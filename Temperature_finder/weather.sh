#!/bin/bash

#Weather Script

latitude=$1
longitude=$2

if [ $# -le 1 ]; 
then
        echo "Please enter both latitude longitude"
        exit
fi

temperature=$(curl -s "https://darksky.net/forecast/$latitude,$longitude/si12/en")
echo "*********************************"
echo -n "Temperature( in ˚C ): "
echo $temperature  | grep -oE '<span class=\"summary swap\">[0-9]*' | grep -oE '[0-9]*$' 
echo "*********************************"
echo -n "Weather : "
echo $temperature  | grep -oE '<span class=\"summary swap\">[^<]*' | grep -oE '[a-zA-Z ]*' | sed '4!d'
echo "*********************************"
#> /home/shubham/Desktop/test.html

