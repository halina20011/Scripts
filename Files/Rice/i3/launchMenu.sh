#!/bin/bash

background=$(jq ".background" ~/.themeScheme.json | tr -d '"')
foreground=$(jq ".foreground" ~/.themeScheme.json | tr -d '"')
sBackground=$(jq ".selectedBackground" ~/.themeScheme.json | tr -d '"')
sForeground=$(jq ".selectedForeground" ~/.themeScheme.json | tr -d '"')
barHeight=$(jq .barHeight ~/.themeScheme.json)
lockImage=$(jq .lockImage ~/.themeScheme.json | tr -d '"')

lockImage=$(eval "echo $lockImage")
echo $lockImage

lockWall="i3lock -i $lockImage -t"

# -nb normal background
# -nf foreground color
# -sb selected color
# -sf selected foreground

DMENU="dmenu -i -h $barHeight -nb $background -nf $foreground -sb $sBackground -sf $sForeground"
choice=$(echo -e "Logout\nShutdown\nReboot\nSuspend\nHibernate\nExit" | $DMENU)

case "$choice" in 
  Exit) i3-msg exit & ;;
  Logout) $lockWall & ;;
  Shutdown) shutdown -h now & ;;
  Reboot) reboot & ;;
  Suspend) $lockWall && systemctl suspend & ;;
  Hibernate) systemctl hibernate & ;;
esac
