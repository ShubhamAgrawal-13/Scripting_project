#!/bin/bash

#File Opener
filepath=$1
if [ "$#" = "0" ];then
	echo "Please enter filepath using command line arguments"
	exit
fi
filetype=$(file -b --mime-type $filepath)
fileapp=$(echo $filetype | cut -d'/' -f1)
# echo $filepath
# echo $filetype
# echo $fileapp

if [ -e $filepath ]; then
	if [ "$filetype" = "text/x-csrc" -o "$filetype" = "text/x-c++src" -o "$filetype" = "text/x-java" -o "$filetype" = "text/plain" -o "$filetype" = "text/x-python" ]; then
		gedit "$filepath"
	elif [ "$filetype" = "image/png" -o "$filetype" = "image/jpeg" -o "$filetype" = "image/bmp" ]; then
		eog "$filepath"
	elif [ "$fileapp" = "image" ]; then
		eog "$filepath"
	elif [ "$filetype" = "audio/mpeg" -o "$filetype" = "audio/wav" -o "$filetype" = "video/x-matroska" -o "$filetype" = "video/mp4" ]; then
		vlc "$filepath"
	elif [ "$fileapp" = "audio" ]; then
		vlc "$filepath"
	elif [ "$filetype" = "video/flv" -o "$filetype" = "video/3gp" -o "$filetype" = "video/webm" -o "$filetype" = "video/avi" ]; then
		vlc "$filepath"
	elif [ "$fileapp" = "video" ]; then
		vlc "$filepath"
	elif [ "$filetype" = "application/pdf" ]; then
		evince "$filepath"
	elif [ "$filetype" = "application/x-sharedlib" ]; then
		($filepath)
	elif [ "$fileapp" = "application" ]; then
		libreoffice "$filepath"
	elif [ "$filetype" = "text/html" ]; then
		firefox "$filepath"
	elif [ "$fileapp" = "text" ]; then
		gedit "$filepath"
	else
		echo "No default application is found"
	fi
else
	echo "File does not exist"
fi

