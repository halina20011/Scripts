import math

INT32_MAX = 2 ** 32 - 1;
INT32_MIN = -(2 ** 32);

def toRad(angle):
    return (angle * math.pi) / 180;

def rotate(angle, p):
    a = toRad(angle);
    s = math.sin(a);
    c = math.cos(a);

    pX = p[0];
    pY = p[1];

    nPX = pX * c - pY * s;
    nPY = pX * s + pY * c;

    return (nPX, nPY);

# line
#  y = c
#  line is horizontal => m = 0;
#  y = c
#
# circle
#  (x - p) ^ 2 + (y - p) ^ 2 = r ^ 2
#  circle in center => p = 0
#  x*x + y*y = r * 2;
# 
#  (x*x) + y*y = r * r
#  x1 = sqrt(r*r - y*y);
#  x1 = -sqrt(r*r - y*y);
def circleGetPoints(y, argv):
    r = argv[0];
    val = r * r - y * y;
    if(val < 0):
        return [0];
    elif(val < 0.00001):
        return [1, 0, 0];

    s = math.sqrt(val);

    return [2, s, -s];

# |-----|
# |  |  |
# |--+--|
# |  |  |
# |-----|
def rectangelGetPoints(y, argv):
    w = argv[0];
    h = argv[1];
    if(y < 0 or h < y):
        return [0];
    
    w2 = w / 2;
    return [2, w2, -w2];

def rectangelCimcumference(x, y, argv, f):
    [w, h] = argv;
    w2 = w / 2;
    h2 = h / 2;
    f.write("G0 X{:.4} Y{:.4}\n".format(x + w2, y + h2));
    f.write("G0 X{:.4} Y{:.4}\n".format(x + w2, y - h2));
    f.write("G0 X{:.4} Y{:.4}\n".format(x - w2, y - h2));
    f.write("G0 X{:.4} Y{:.4}\n".format(x - w2, y + h2));
    f.write("G0 X{:.4} Y{:.4}\n".format(x + w2, y + h2));

def circleCircCimcumference(x, y, argv, f):
    [radius, resolution] = argv;
    # print(resolution);
    for i in range(resolution + 1):
        angle = 360 / resolution * i;
        rAngle = toRad(angle);
        xP = math.cos(rAngle) * radius + x;
        xY = math.sin(rAngle) * radius + y;
        # print(xP, xY);
        
        f.write("G0 X{:.4} Y{:.4}\n".format(xP, xY));

def rectangleInside(x, y, w, h, px, py):
    w2 = w / 2;
    h2 = h / 2;
    
    insideX = (x - w2 <= px and px <= x + w2);
    insideY = (y - h2 <= py and py <= y + h2);

    return insideX and insideY;

def circleInside(x, y, w, h, px, py):
    X = px - x;
    Y = py - y;
    d = math.sqrt(X * X + Y * Y);
    return d <= w/2; 

# def rectangelProbePoints(x, y, argv, step, f):
#     [h, w] = argv;
#     # one 
#     yOffset = 0.0;
#     f.write("G0 Z2\n");
#     while(True):
#         if(h < yOffset):
#             yOffset = h;
#
#         xOffset = 0;
#         while(True):
#             if(h < xOffset):
#                 xOffset = h;
#             f.write("G0 X{:.4} Y{:.4}\n".format(x + xOffset, y + yOffset));
#             f.write("G0 Z-2\n");
#             f.write("G0 Z2\n");
#             
#             xOffset += step;
#
#             if(yOffset == h):
#                 break;
#         
#         yOffset += step;
#         if(yOffset == h):
#             break;
#     
#     # move up
#     f.write("G0 Z{:.4}\n".format(0.2));

# 1         2
# -----------
# |         |
# |         |
# |         |
# ----------- 3
# 4
class SquareMins:
    def __init__(self):
        self.minX = INT32_MAX;
        self.maxX = INT32_MIN;
        
        self.leftYMin = INT32_MAX;
        self.leftMax = None;
        self.leftMin = None;
        self.leftYMax = INT32_MIN;

        self.rightYMin = INT32_MAX;
        self.rightMax = None;
        self.rightMin = None;
        self.rightYMax = INT32_MIN;

    def get(self):
        return [self.leftMax, self.leftMin];

    def update(self, x, y, item):
        print(x, y);
        if(x <= self.minX):
            self.minX = x;
            if(self.leftYMax < y):
                y = self.leftYMax;
                self.leftMax = item;
            if(y < self.leftYMin):
                y = self.leftYMin;
                self.leftMin = item;
        
        # if(self.maxX <= x):
        #     self.maxX = x;
        #     if(self.rightYMax < y):
        #         y = self.rightYMax;
        #         self.rightMax = item;
        #     if(y < self.rightYMin):
        #         y = self.rightYMin;
        #         self.rightMin = item;

class BoundingBox:
    def __init__(self):
        self.minX = INT32_MAX;
        self.maxX = INT32_MIN;
        self.minY = INT32_MAX;
        self.maxY = INT32_MIN;

    def update(self, x, y):
        if(x < self.minX):
            self.minX = x;
        
        if(self.maxX < x):
            self.maxX = x;

        if(y < self.minY):
            self.minY = y;
        
        if(self.maxY < y):
            self.maxY = y;

    def size(self):
        w = self.maxX - self.minX;
        h = self.maxY - self.minY;
        return (w, h);
