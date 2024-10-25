#!/usr/bin/env python
import sys
from pcbnew import *
import re
import json

from shape import *

mmToMils = 1000000

CIRCLE = 0;
RECTANGLE = 1;
OVAL = 2;
ROUNDED_RECTANGLE = 4;

def dist(x, y):
    return x * x + y * y;
#
# MINIMAZE = 0;
# MAXIMAZE = 1;
#
# def extreme(type, curr, val):
#     if(type == MINIMAZE):
#         return min(curr, val);
#     return max(curr, val);
#
# class MM:
#     def __init__(self, xType, yType):
#         self.xType = xType;
#         self.yType = yType;
#
#         self.x = INT32_MIN if(xType == MAXIMAZE) else INT32_MAX;
#         self.y = INT32_MIN if(yType == MAXIMAZE) else INT32_MAX;
#         
#     # the x axis always has the bigger 
#     def update(self, x, y, item):
#         extremeX = extreme(self.xType, self.x, x);
#         extremeY = extreme(self.yType, self.y, y);
#         if(abs(extremeX - x) < abs(extremeX - self.x)):

def ceiling(x):
    n = int(x);
    return n if n - 1 < x <= n else n + 1;

def fixed(n, d):
    d = 10 ** d;
    return ceiling(n * d) / d;

class Pad:
    def __init__(self, tuttplePosition, tuttpleSize, shape, isSmd):
        self.shape = shape;
        self.x = tuttplePosition[0] / mmToMils;
        self.y = tuttplePosition[1] / mmToMils;
        self.w = tuttpleSize[0] / mmToMils;
        self.h = tuttpleSize[1] / mmToMils;

        self.isSmd = isSmd;

        self.offsetX = 0;
        self.offsetY = 0;

    def X(self, x):
        return fixed(self.x + x, 5);

    def Y(self, y):
        return fixed(self.y + y, 5);

    def getPoint(self, p, c):
        d = p - c;
        # print(p, c, d);
        # print(f"point {p} cursor {c}");
        return c - d;

    def setCursorX(self, x):
        self.x = self.getPoint(self.x, x);
        # print(f"res {self.x}");

    def setCursorY(self, y):
        self.y = self.getPoint(self.y, y);

    def offset(self, offsetX, offsetY):
        self.x += offsetX;
        self.y += offsetY;

    def rotate(self, angle):
        (self.x, self.y) = rotate(angle, (self.x, self.y));

    def __str__(self):
        return f"Pad[{self.isSmd}][{self.X(0)} {self.Y(0)}]";


INT32_MAX = 2 ** 32 - 1;
INT32_MIN = -(2 ** 32);

class MinPad():
    def __init__(self):
        self.x = INT32_MIN;
        self.y = INT32_MAX;
        self.d = INT32_MAX;

    def update(self, x, y):
        d = math.sqrt(x * x + y * y);
        if(d < self.d):
            self.x = x;
            self.y = y;
            self.d = d;

class MaxPad():
    def __init__(self):
        self.x = None;
        self.y = None;
        self.d = INT32_MIN;

    def update(self, x, y):
        d = math.sqrt(x * x + y * y);
        if(self.d < d):
            print("new", x, y);
            self.x = x;
            self.y = y;
            self.d = d;

# TODO: scientific notations wont be matched
pattern = r"G0 X([-+]?[0-9][*\.[0-9]+]?)\s?Y([-+]?[0-9][*\.[0-9]+]?)";
def getMinDrillPos(drillNgcFile, offsetX, offsetY, angle):
    drl = open(drillNgcFile, "r");
    minPad = MinPad();
    for line in drl:
        match = re.match(pattern, line);
        if(match):
            x = float(match.group(1)) - offsetX;
            y = float(match.group(2)) - offsetY;
            # [pX, pY] = rotate(angle, x, y);
            d = dist(x, y);
            print("drill pos => ", x, y, d);
            minPad.update(x, y);

    return minPad;

class Pos:
    def __init__(self, tupple):
        self.x = tupple[0] / mmToMils;
        self.y = tupple[1] / mmToMils;

    def __str__(self):
        return f"[{self.x} {self.y}]";

# file with .pcb
def main():
    argv = sys.argv;
    if(len(argv) == 1):
        print("pcb file has to be specified");
        return;
    fileName = sys.argv[1];
    print("file: " + fileName);

    pcb = LoadBoard(fileName);

    # print(Pos(pcb.GetBoardEdgesBoundingBox().GetSize()));
    bebb = pcb.GetBoardEdgesBoundingBox();
    pcbSize = Pos([bebb.GetWidth(), bebb.GetHeight()]);
    print("pcbSize: ", pcbSize);

    pcbOffsetX = pcb.GetBoundingBox().GetX() / mmToMils;
    pcbOffsetY = pcb.GetBoundingBox().GetY() / mmToMils;
    print("boardOffset: ", pcbOffsetX, pcbOffsetY);

    rotAngle = 180;
    # minDrillPos = None
    minDrillPos = getMinDrillPos(sys.argv[2], 0, 0, rotAngle) if (len(argv) == 3) else [None, None];

    fileName = "output.gcode";
    file = open(fileName, "w+");
    if(file == None):
        print(f"failed to open {fileName}");
        return;

    pads = [];
    minPad = MinPad();
    maxPad = MaxPad();
    for pad in pcb.GetPads():
        size = pad.GetSize();
        pos = pad.GetPosition();
        shape = pad.GetShape();
        isSmd = pad.GetDrillSizeX() == 0;

        # rotatedPos = rotate(180, pos);
        # newPad = Pad(rotatedPos, size, shape, isSmd);
        newPad = Pad(pos, size, shape, isSmd);
        newPad.offset(-pcbOffsetX, -pcbOffsetY);
        newPad.offset(0, -pcbSize.y);
        # newPad.rotate(-90);
        # newPad.rotate(-90);
        newPad.rotate(180);
        # newPad.rotate(89.9);
        # newPad.offset(0, 0);
        # addPoint(newPad.x, newPad.y, "red");

        # plt.axhline(pcbSize.x / 2, color="yellow");
        # plt.axvline(pcbSize.x / 2, color="yellow");

        # newPad.setCursor(pcbSize.x / 2, pcbSize.y / 2);
        
        # print(f"cursor {x}");
        # newPad.setCursorX(pcbSize.x / 2);
        # newPad.setCursorY(pcbSize.y / 2);

        # addPoint(newPad.x, newPad.y, "blue");
        # rect(newPad.x, newPad.y, newPad.w, newPad.h, "none");
        # newPad.setCursorX(0);
        # newPad.setCursorY(pcbSize.y / 2);
        # newPad.setCursor(pcbSize.x / 2, 0);
        # newPad.offset(-17.51, 0);
        
        # print(newPad);
        
        pads.append(newPad);
        if(not isSmd):
            minPad.update(newPad.x, newPad.y);
            print(newPad.x, newPad.y);
            maxPad.update(newPad.x, newPad.y);
    
    if(minPad == None):
        return;

    # addPoint(minPad.x, minPad.y, "black");
    print("min pad {} {}".format(minPad.x, minPad.y));

    offsetX = 0;
    offsetY = 0;

    # minDrillPos = None;
    if(minDrillPos):
        print("minDrillPos", minDrillPos.x, minDrillPos.y);
        offsetX = minDrillPos.x - minPad.x;
        offsetY = minDrillPos.y - minPad.y;

    # offsetY = 0.5;
    # offsetX = 20;
    print(minDrillPos);
    print(offsetX, offsetY);

    file.write("G94 (mm/min feed rate)\n");
    file.write("G21 (units mm)\n");
    file.write("G90 (Absolute coordinates)\n");
    file.write("G01 F20.0 (feedrate)\n");

    file.write("G01 Z2.0 (Move up)\n");
    file.write("G01 X0 Y0 (Origin)\n");

    probeInfo = {};

    step = 0.08;
    boundingBox = BoundingBox();
    for i, p in enumerate(pads):
        p.offset(offsetX, offsetY);
        # p.offset(0, -0.5);
        # p.setCursor(pcbSize.x / 2, pcbSize.y / 2);
        # p.setOffset(offsetX, offsetY);

        x = p.X(0);
        y = p.Y(0);

        file.write("(hole:[{}][X{:.4f} Y{:.4f}]<{:.4f},{:.4f}>)\n".format(p.shape, p.X(0), p.Y(0), p.w, p.h));
        file.write("G01 Z2.0 (Move up)\n");
        file.write("(hole: {})\n".format(i));
        f = None; start = None; end = None; argv = None;
        fC = None; argvC = None;
        if(p.shape == CIRCLE or p.shape == OVAL):
            f = circleGetPoints;
            fC = circleCircCimcumference;
            argv = [p.w/2];
            argvC = [p.w/2, 40];
            start = -p.h / 2;
            end = -start;
        elif(p.shape == RECTANGLE or p.shape == ROUNDED_RECTANGLE):
            p.offset(0, -p.h/2);
            f = rectangelGetPoints;
            fC = rectangelCimcumference;
            # start = 0;
            # end = p.h;
            start = 0;
            end = p.h;
            argv = [p.w, p.h];
            argvC = [p.w, p.h];
        else:
            print("not implemented shape: {}".format(p.shape));
            continue;

        # print(start, end)
        i = start;
        side = True;
        down = False;
        while(i < end):
            i += step;
            points = f(i, argv);
            size = points[0];
            # print(points);
            # print(p.shape);
            if(size == 2):
                x1 = points[1]; x2 = points[2];
                if(side == False):
                    (x1, x2) = (x2, x1);

                side = not side;
                
                file.write("G0 X{:.4} Y{:.4}\n".format(p.X(x1), p.Y(i)));
                if(not down):
                    file.write("G01 Z0.0 (Move down)\n");
                    down = True;
                file.write("G0 X{:.4} Y{:.4}\n".format(p.X(x2), p.Y(i)));

                boundingBox.update(p.X(x1), p.Y(i));
                boundingBox.update(p.X(x2), p.Y(i));

        # generate shape circumstance
        file.write("(shape circumstance)");
        fC(x, y, argvC, file);

    percision = 0.7;
    (w, h) = boundingBox.size();
    minX = boundingBox.minX;
    minY = boundingBox.minY;
    stepsX = math.ceil(w / percision);
    stepsY = math.ceil(h / percision);

    print(f"size [{w}x{h}] steps [{stepsX}x{stepsY}]");

    probeInfo["info"] = {};
    probeInfo["info"]["percision"] = percision;
    probeInfo["info"]["minX"] = minX;
    probeInfo["info"]["minY"] = minY;
    probeInfo["info"]["w"] = w;
    probeInfo["info"]["h"] = h;
    probeInfo["info"]["stepsX"] = stepsX;
    probeInfo["info"]["stepsY"] = stepsY;

    probeInfo["points"] = {};
    probePoints = 0;
    for PY in range(stepsY):
        probeInfo["points"][PY] = {};
        for PX in range(stepsX):
            boolInside = False;
            px = PX * percision + minX;
            py = PY * percision + minY;
            # print(px, py)
            for p in pads:
                x = p.X(0);
                y = p.Y(0);
                if(p.shape == CIRCLE or p.shape == OVAL):
                    if(circleInside(x, y, p.w, p.h, px, py)):
                        boolInside = True;
                        # print("inside");
                        break;
                elif(p.shape == RECTANGLE or p.shape == ROUNDED_RECTANGLE):
                    if(rectangleInside(x, y, p.w, p.h, px, py)):
                        # print("inside");
                        boolInside = True;
                        break;

            if(boolInside):
                probePoints += 1;

            probeInfo["points"][PY][PX] = boolInside;

    # export probeInfo
    with open("probeInfo.json", "w") as f:
        json.dump(probeInfo, f);
    
    print(f"number of points to probe {probePoints}");

if __name__ == "__main__":
    main();
