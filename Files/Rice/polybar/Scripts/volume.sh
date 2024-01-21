#!/bin/bash

info=""

# Master
master=($(amixer get Master | grep "Mono:"))
masterStatus=${master[${#master[@]} - 1]}

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


# printf "Master              $masterStatus\n"
#
# printf "Speaker             $speakerStatus\n"
# printf "Speaker Left        $speakerStatusLeft\n"
# printf "Speaker Rigth       $speakerStatusRight\n"
#
# printf "Headphone left:     $headphoneStatusLeft\n"
# printf "Headphone right:    $headphoneStatusRight\n"

if [[ ${masterStatus} == "[off]" ]]; then
    printf "off\n"
    exit 0
fi

function parseV(){
    echo $(echo $1 | tr -d '[]')
}

if [[ ${masterStatus} == "[on]" ]]; then
    info="$(parseV ${master[3]})"

    if [[ $headphoneStatus == "[on]" ]]; then
        info="$info H: $(parseV ${headphoneLeft[4]})"

    elif [[ $speakerStatus == "[on]" ]]; then
        info="$info S: $(parseV ${speakerLeft[4]})"
        
    else
        info="Error ;)"
    fi
else
    echo "Error ;)"
fi

echo $info

exit 0
