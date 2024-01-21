#!/bin/bash
# ./volumeControl.sh [up/down/toggle] [/shift]

# echo $@

if [[ $1 == "up" ]] && [[ $2 != "shift" ]]; then
    (amixer sset Master -R 2%+)
    exit 0
elif [[ $1 == "down" ]] && [[ $2 != shift ]]; then
    (amixer sset Master -R 2%-)
    exit 0
elif [[ $1 == "toggle" ]] && [[ $2 != shift ]]; then
    (amixer sset Master toggle)
    exit 0
fi

# Speaker
speakerLeft=($(amixer get Speaker | grep "Front Left:"))
speakerRight=($(amixer get Speaker | grep "Front Right:"))

speakerStatusLeft="${speakerLeft[${#speakerLeft[@]} - 1]}"
speakerStatusRight="${speakerRight[${#speakerRight[@]} - 1]}"

speaker=""
speakerStatus=""

if [ "$speakerStatusLeft" == "$speakerStatusRight" ] && [ $speakerStatusLeft == "[on]" ]; then
    speaker=$(echo $speakerLeft)
    speakerStatus="[on]"
fi 

# Headphone
headphoneLeft=($(amixer get Headphone | grep "Front Left:"))
headphoneRight=($(amixer get Headphone | grep "Front Right:"))

headphoneStatusLeft=${headphoneLeft[${#headphoneLeft[@]} - 1]}
headphoneStatusRight=${headphoneRight[${#headphoneRight[@]} - 1]}

headphone=""
headphoneStatus=""


if [ $headphoneStatusLeft == $headphoneStatusRight ] && [ $headphoneStatusLeft == "[on]" ]; then
    headphone=$(echo $headphoneStatusLeft)
    headphoneStatus="[on]" 
fi 

device=""
if [[ $speakerStatus == "[on]" ]]; then
    device="Speaker"
elif [[ $headphoneStatus == "[on]" ]]; then
    device="Headphone"
fi

if [[ $device == "" ]]; then
    exit 1
fi

if [[ $1 == "up" ]] && [[ $2 == "shift" ]]; then
    (amixer sset ${device} -R 2%+)
    exit 0
elif [[ $1 == "down" ]] && [[ $2 == shift ]]; then
    (amixer sset ${device} -R 2%-)
    exit 0
elif [[ $1 == "toggle" ]] && [[ $2 == shift ]]; then
    (amixer sset ${device} toggle)
fi
