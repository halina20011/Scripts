pcbFile = ~/EE/DeskLamp/DeskLampCircuit/DeskLampCircuit.kicad_pcb
drillFile = ~/EE/DeskLamp/DeskLampCircuit/Output/drill.ngc
outputFolder = ~/EE/DeskLamp/DeskLampCircuit/Output
# pcbFile = ~/EE/KiCad/TestBoard/testBoard.kicad_pcb
# drillFile = ~/EE/KiCad/TestBoard/Output/drill.ngc
# outputFolder = ~/EE/KiCad/TestBoard/Output/

run:
	python3 src/main.py $(pcbFile) $(drillFile)
	cp output.gcode /tmp
	# python3 src/main.py $(pcbFile)

mergeBack: run
	cat $(outputFolder)/back.ngc > /tmp/merged.ngc;
	echo "\n" >> /tmp/merged.ngc;
	cat output.gcode >> /tmp/merged.ngc

mergeDrill: run
	cat $(outputFolder)/drill.ngc > /tmp/merged.ngc;
	echo "\n" >> /tmp/merged.ngc;
	cat output.gcode >> /tmp/merged.ngc
