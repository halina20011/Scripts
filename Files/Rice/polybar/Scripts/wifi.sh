#!/bin/bash
interfaces=$(ip addr | grep -Eo --color '^[0-9]: [^:]*')

# \d is not supported
interfacesArray=( $(echo $interfaces | sed -E --expression="s/[0-9]: / /g") )
echo ${interfacesArray[@]}
interfacesEnpWlp=( $(echo ${interfacesArray[@]} | grep -Eo "(enp|wlp)\w*") )
echo Ethernet and wireless adapters: ${interfacesEnpWlp[@]}
