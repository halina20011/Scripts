#!/bin/python

import subprocess
import os
import json

jsonFile = os.path.join(os.path.dirname(__file__), "files.json");

def safePath(path):
    return os.path.expanduser(path);

def copy(source, des):
    command = ["cp", "-r", safePath(source), safePath(des)];
    print(command);
    try:
        subprocess.run(command)
        print(f"{source} =>{des}");
    except subprocess as e:
        print(f"Error copying files: {e}")

def read():
    with open(jsonFile, "r") as file:
        return json.load(file);

if __name__ == "__main__":
    array = read()["array"];
    for item in array:
        print(item);
        source = item["s"];
        destination = item["d"];
        copy(source, destination);
