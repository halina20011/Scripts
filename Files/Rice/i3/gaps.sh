#!/bin/bash

background=$(jq ".background" ~/.themeScheme.json | tr -d '"')
foreground=$(jq ".foreground" ~/.themeScheme.json | tr -d '"')
sBackground=$(jq ".selectedBackground" ~/.themeScheme.json | tr -d '"')
sForeground=$(jq ".selectedForeground" ~/.themeScheme.json | tr -d '"')
barHeight=$(jq .barHeight ~/.themeScheme.json)

# -nb normal background
# -nf foreground color
# -sb selected color
# -sf selected foreground

DMENU="dmenu -i -h $barHeight -nb $background -nf $foreground -sb $sBackground -sf $sForeground"
# Gaps: (o)uter, (i)nner, (h)orizontal, (v)ertical, (t)op, (r)ight, (b)ottom, (l)eft
choice=$(echo -e "outer\ninner\nhorizonatl\nvertical\ntop\nright\nbottom\nleft" | $DMENU)

case "$choice" in
  outer) i3-msg exit & ;;
  inner) $lockWall & ;;
  vertical) sudo shutdown -h now & ;;
  top) sudo shutdown -r now & ;;
  right) $lockWall && systemctl suspend & ;;
  bottom) systemctl hibernate & ;;
  left) 
esac
