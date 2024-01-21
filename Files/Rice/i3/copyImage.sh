path=/home/mario/Documents/Pictures/Screenshots/.tmp.png

import $path

xclip -selection clipboard -target image/png -i < ${path}

rm $path
