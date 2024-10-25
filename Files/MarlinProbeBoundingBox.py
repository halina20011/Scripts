from ..Script import Script
from UM.Application import Application
from UM.Logger import Logger

from UM.Application import Application
from UM.Scene.Iterator.DepthFirstIterator import DepthFirstIterator

import datetime
import os

import inspect

def custom_help(obj):
    print(f"Type:\n  {type(obj)}\n")
    
    # Print documentation if available
    print("Documentation:")
    if obj.__doc__:
        print(" ", obj.__doc__)
    else:
        print("  No documentation available.")
    print("\n" + "="*40)
    
    # Print attributes and methods
    print("Attributes and Methods:")
    members = dir(obj)
    if members:
        for member in members:
            print("  ", member)
    else:
        print("  No attributes or methods found.")
    print("\n" + "="*40)
    
    # Print class attributes if it's a class instance
    if hasattr(obj, "__dict__"):
        print("Class Attributes (from __dict__):")
        for attr, value in vars(obj).items():
            print(f"  {attr}: {value}")
    else:
        print("No instance-specific attributes available.")
    print("\n" + "="*40)
    
    # Show inheritance if applicable
    if hasattr(obj, "__class__"):
        print("Inheritance (MRO):")
        mro = inspect.getmro(obj.__class__)
        for cls in mro:
            print(f"  {cls}")
    print("\n" + "="*40)
    
    # Print source code if it's a class or function and source is available
    try:
        print("Source Code:")
        source = inspect.getsource(obj)
        print(source)
    except (TypeError, OSError):
        print("  Source code not available.")

class CustomDebugger:
    def __init__(self, log_file_path="/tmp/debug.log"):
        # Open a file stream for debugging
        self.log_file = open(log_file_path, "w")

    def log(self, message):
        """Write a message to the debug file with a timestamp."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.log_file.write(f"{timestamp} - {message}\n")
        self.log_file.flush()  # Ensure the message is written to the file immediately

    def close(self):
        """Close the debug file."""
        self.log_file.close()

class BoundingBox:
    def __init__(self):
        # Initialize with None to handle first point addition smoothly
        self.min_x = None
        self.min_y = None
        self.max_x = None
        self.max_y = None

    def add_point(self, x, y):
        # If it's the first point, set min and max to this point's coordinates
        if self.min_x is None or self.min_y is None:
            self.min_x = self.max_x = x
            self.min_y = self.max_y = y
        else:
            # Update the min and max values
            self.min_x = min(self.min_x, x)
            self.min_y = min(self.min_y, y)
            self.max_x = max(self.max_x, x)
            self.max_y = max(self.max_y, y)

    def get_min(self):
        return (self.min_x, self.min_y)

    def get_max(self):
        return (self.max_x, self.max_y)

    def get_bounding_box(self):
        # Returns the min and max coordinates as a tuple
        return (self.min_x, self.min_y, self.max_x, self.max_y)

    def __str__(self):
        # String representation for easy printing
        return f"BoundingBox(min=({self.min_x}, {self.min_y}), max=({self.max_x}, {self.max_y}))"

import re

class TagParser:
    # Define allowed tags as a set of lowercase strings
    ALLOWED_TAGS = {"minx", "miny", "minz", "maxx", "maxy", "maxz"}

    def __init__(self):
        # Dictionary to hold only allowed parsed tags
        self.tags = {}

    def parse_line(self, line):
        # Regular expression to match the pattern ;TAG:value
        match = re.match(r";(\w+):([\d.]+)", line.strip())
        if match:
            tag, value = match.groups()
            tag = tag.lower()  # Convert tag to lowercase
            if tag in self.ALLOWED_TAGS:  # Only store if tag is allowed
                self.tags[tag] = float(value)  # Convert value to float

    def parse_lines(self, lines):
        # Parse multiple lines
        for line in lines:
            self.parse_line(line)

    def get_tag(self, tag_name):
        # Get the value of a tag by name, or None if not found
        return self.tags.get(tag_name.lower())

    def __str__(self):
        # String representation for debugging and viewing tags
        return f"Parsed tags: {self.tags}"

class MarlinProbeBoundingBox(Script):
    def __init__(self):
        super().__init__()

    def getSettingDataString(self):
        return """{
            "name": "Marlin Probe Bounding Box",
            "key": "MarlinProbeBoundingBox",
            "metadata": {},
            "version": 2,
            "settings":
            {
                "probeNumber":
                {
                    "label": "Number of probes",
                    "description": "Number of probes for x/y axis",
                    "unit": "mm",
                    "type": "int",
                    "default_value": 4,
                    "minimum_value": "2",
                    "minimum_value_warning": "2",
                    "maximum_value_warning": "200"
                }
            }
        }"""
                # "minX":
                # {
                #     "label": "min probe x",
                #     "unit": "mm",
                #     "type": "int",
                #     "default_value": 52,
                #     "minimum_value": "0",
                #     "maximum_value": "400",
                # },
                # "minY":
                # {
                #     "label": "min probe y",
                #     "unit": "mm",
                #     "type": "int",
                #     "default_value": 32,
                #     "minimum_value": "0",
                #     "maximum_value": "400",
                # },
                # "maxX":
                # {
                #     "label": "max probe x",
                #     "unit": "mm",
                #     "type": "int",
                #     "default_value": 232,
                #     "minimum_value": "0",
                #     "maximum_value": "400",
                # },
                # "maxY":
                # {
                #     "label": "max probe y",
                #     "unit": "mm",
                #     "type": "int",
                #     "default_value": 222,
                #     "minimum_value": "0",
                #     "maximum_value": "400",
                # }

    def sliceableNodes(self):
        # Add all sliceable scene nodes to check
        scene = Application.getInstance().getController().getScene()
        for node in DepthFirstIterator(scene.getRoot()):
            if node.callDecoration("isSliceable"):
                yield node

    def _absBox(self, node):
        bounding_box = node.getBoundingBox()
        center_local = bounding_box.center()

        # Get the world transformation matrix of the object
        transformation_matrix = node.getWorldTransformation()

        # Transform the center point to world coordinates
        center_world = transformation_matrix * center_local  # Matrix multiplication

        # Print or return the absolute center position
        Logger.log("d", f"Absolute Position on Printer Bed - X: {center_world.x}, Y: {center_world.y}, Z: {center_world.z}")
        return center_world

    def _move(self, absPos, pos, axis, val):
        if(absPos):
            pos[axis] = val;
        else:
            pos[axis] += val;

    def _calculate_bounding_box(self, data):
        # bb = BoundingBox();
        #
        # pos = {"x": 0, "y":0};
        # absPos = True;
        
        tags = TagParser();

        for item in data:
            Logger.log("d", item);
            for line in item.split("\n"):
                tags.parse_line(line);

                # command = line.split(";")[0];
                # 
                # if(len(command) == 0):
                #     continue;
                #
                # if("G90" in command):
                #     absPos = True;
                # elif("G91" in command):
                #     absPos = False;
                #
                # G0 = "G0" in command;
                # G1 = "G1" in command;
                # Logger.log("d", f"G0 {G0} G1 {G1} in '{command}'");
                # if(G0 or G1):
                #     for arg in command.split(" "):
                #         if(len(arg) == 0):
                #             continue;
                #
                #         Logger.log("d", arg);
                #         t = arg[0].lower();
                #         if(t in pos):
                #             val = float(arg[1:]);
                #             self._move(absPos, pos, t, val);
                #     Logger.log("d", pos);
                #     bb.add_point(pos["x"], pos["y"]);
        # Logger.log("d", bb.get_bounding_box());
        Logger.log("d", tags.tags);
        t = tags.tags;
        
        return {
                "min": [t["minx"], t["miny"], t["minz"]], 
                "max": [t["maxx"], t["maxy"], t["maxz"]]
        };

        # scene = Application.getInstance().getController().getScene()
        # nodes = self.sliceableNodes();
        #
        # for node in nodes:
        #     custom_help(node);
        #     self._absBox(node);
        #     # position = node.getPosition();
        #     # bbox = node.getBoundingBox();
        #     # wPos = node.getWorldPosition();
        #     # wT = node.getWorldTransformation();
        #     # Logger.log("d", wPos);
        #     # Logger.log("d", wT);
        #     # Logger.log("d", position);
        #     # Logger.log("d", bbox);

        # # node = scene.getRoot().getChildren()[0]  # Assumes the main model is the first child
        # children = scene.getRoot().getChildren();
        # Logger.log("d", children);
        # for node in children:
        #     # custom_help(node);
        #     # Logger.log("d", node)
        #     bbox = node.getBoundingBox()
        #     Logger.log("d", bbox)

        # if isinstance(node, CuraSceneNode):
        #     bounds = node.getBoundingBox()
        #     self.bounding_box = {
        #         'width': bounds.width(),
        #         'height': bounds.height()
        #     }
        #     
        #     Logger.log("d", "Bounding box - Width: {self.bounding_box['width']}, Height: {self.bounding_box['height']}")

    # ;PROBE_POSITION
    def _insertProbe(self, data, probeCommand):
        Logger.log("d", probeCommand);
        for i, item in enumerate(data):
            Logger.log("d", item);
            if("PROBE_POSITION" in item):
                data[i] = item.replace(";PROBE_POSITION", probeCommand);
        
        return data;

    def execute(self, data):
        probeNumber = self.getSettingValueByKey("probeNumber");
        # Logger.log("d", data);
        Logger.log("d", "uwuwuwuwuwuwuwuwu");

        bb = self._calculate_bounding_box(data);
        Logger.log("d", bb);
        probeCommand = f"G29 X{probeNumber} Y{probeNumber} L{bb['min'][0]} R{bb['max'][0]} F{bb['min'][1]} B{bb['max'][1]} T V4\nG1 Z5 F300\nG1 X0 Y0 F4000"
        data = self._insertProbe(data, probeCommand);
        # for layer in data:
        #     Logger.log("d", layer);

        # width = self.getSettingValueByKey("")
        # Logger.log("d", "uwu");
        # text = "M501 ;load bed level data\nM420 S1 ;enable bed leveling"
        # if self.getSettingValueByKey("use_previous_measurements"):
        #     for layer in data:
        #         layer_index = data.index(layer)
        #         lines = layer.split("\n")
        #         for line in lines:
        #             if line.startswith("G29"):
        #                 line_index = lines.index(line)
        #                 lines[line_index] = text
        #         final_lines = "\n".join(lines)
        #         data[layer_index] = final_lines
        # data.append("");
        return data
