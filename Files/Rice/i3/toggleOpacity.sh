picomPid=$(pidof picom)
#echo $picomPid

if [[ $picomPid == "" ]]; then
    echo "Starting picom"
    picom &
else 
    echo "killing picom"
    kill $picomPid
fi
