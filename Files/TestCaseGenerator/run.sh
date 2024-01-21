#!/bin/sh
node main.js | tee /dev/tty | xclip -sel clip
