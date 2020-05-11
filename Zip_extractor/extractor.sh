#!/bin/bash

#File Extractor

filepath=$1


if [ $# -eq 0 ]; 
then
        echo "Please enter the filepath using command line arguments"
        exit
fi

filetype=$(file -b --mime-type $filepath)

if [ -e $filepath ]; then
	fileExt=$( echo $filepath | grep -oE "\.tar\.gz$" )
	#echo $fileExt
	if [ "$fileExt" = ".tar.gz" ]; then
	    tar xvzf "$filepath"
	else
		fileExt=$( echo $filepath | grep -oE "\.tar\.bz2$" )
		echo $fileExt
		if [ "$fileExt" = ".tar.bz2" ]; then
		    tar xjvf "$filepath"
		else
			fileExt=$( echo $filepath | sed 's/.*\.//' )
			#echo $fileExt
			if [ "$fileExt" = "tar" ]; then
				tar xf "$filepath"
			elif [ "$fileExt" = "tgz" ]; then
				tar xvzf "$filepath"
			elif [ "$fileExt" = "tbz2" ]; then
				tar xjvf "$filepath"
			elif [ "$fileExt" = "gz" ]; then
				gunzip "$filepath"
			elif [ "$fileExt" = "bz2" ]; then
				bunzip "$filepath"
			elif [ "$fileExt" = "zip" ]; then
				unzip "$filepath"
			elif [ "$fileExt" = "7z" ]; then
				7z x "$filepath"
			elif [ "$fileExt" = "rar" ]; then
				rar x "$filepath"
			else
				echo "-----------File cannot be extracted-------------"
			fi
		fi
	fi
else
	echo "-----------------File does not exist-----------------"
fi
echo "-------File Extracted Successfully---------"
