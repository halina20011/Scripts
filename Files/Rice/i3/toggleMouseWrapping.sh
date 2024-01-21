#!/usr/bin/

i3Config=/home/mario/.config/i3/config

if [[ ! -f $i3Config ]]; then
    notify-send "i3 config file does not exist" && exit -1
fi 
echo "a"
mouseWarping=$(awk '$1 == "mouse_warping" {print $2; exit}' $i3Config)

echo $mouseWarping

newMouseWarping=""

if [[ $mouseWarping == "none" ]]; then
    newMouseWarping="mouse_warping output"
else
    newMouseWarping="mouse_warping none"
fi

echo "newValue: $newMouseWarping"

sed -i "s/mouse_warping.*/${newMouseWarping}/" $i3Config
