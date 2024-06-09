import sys
from serial import Serial
import json
import time
import re

def waitForIdle(serial):
    idleCounter = 0;
    while True:
        serial.reset_input_buffer();
        serial.write(f"?\n".encode());
        response = serial.readline().strip().decode("utf-8");

        if(response != "ok"):
            if(0 < response.find("Idle")):
                idleCounter += 1;

        if(3 < idleCounter):
            break;

# def waitForIdle(serial):
#     while True:
#         serial.write(f"?\r\n".encode());
#         idle = False; run = False;
#
#         # wait for response
#         while(not idle and not run):
#             response = serial.readline().decode("utf-8").strip();
#             print(f">>{response}");
#             if(response.startswith("error")):
#                 raise Exception(response);
#
#             idle = re.match(isIdle, response);
#             run = re.match(isRun, response);
#             # print("regex", idle, run);
#
#         if(idle and not run):
#             break;
#         time.sleep(0.1);
#

def send(serial, command):
    print(command);
    serial.write(f"{command}\r\n".encode());
    waitForIdle(serial);
    r = serial.readline().strip().decode("utf-8");
    print(f">> {r}");
    # while True:
    #     response = serial.readline().decode("utf-8").strip();
    #     match = re.match(pattern, response);
    #     print(f">>{response}");
    #     if(response.startswith("error")):
    #         raise Exception(response);
    #     elif(match):
    #         break;
    #     # else:
    #     #     raise Exception("~nyaaa");

def main():
    argv = sys.argv;
    if(len(argv) == 2):
        print("missing args [json] [device]");
        return;
    
    probeInfoFile  = sys.argv[1];
    device  = sys.argv[2];

    probeInfo = {};
    with open(probeInfoFile) as f:
        probeInfo = json.load(f);

    print(probeInfo["info"])
    percision = probeInfo["info"]["percision"];
    minX = probeInfo["info"]["minX"];
    minY = probeInfo["info"]["minY"];

    stepsX = probeInfo["info"]["stepsX"];
    stepsY = probeInfo["info"]["stepsY"];

    with Serial(device, 115200, timeout=2) as serial:
        serial.write("\r\n\r\n".encode());
        time.sleep(2);
        serial.flushInput();

        send(serial, "G94");
        send(serial, "G21");
        send(serial, "G90");
        send(serial, "G10L20P1X0Y0Z0");
        send(serial, "G1 F400.0");
        
        send(serial, "G1 Z1 F100");
        send(serial, "G38.2 Z-20 F10");
        send(serial, "G10 L20 P1 Z0");
        send(serial, "G1 F500 Z2");
        with open("info.probe", "w") as f:
            for PY in range(stepsY):
                for PX in range(stepsX):
                    px = PX * percision + minX;
                    py = PY * percision + minY;
                    command = "G1 X{:.5} Y{:.5}".format(px, py);
                    print(command);
                    send(serial, command);

if __name__ == "__main__":
    main();
