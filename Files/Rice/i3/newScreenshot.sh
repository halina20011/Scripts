name="Screenshot"

dir=/home/mario/Documents/Pictures/Screenshots/
file=(/home/mario/Documents/Pictures/Screenshots/*.png)

newFileNumber=$(( ${#file[@]}+1 ))
newFile=${dir}$name$newFileNumber.png

import $newFile

echo $newFile

