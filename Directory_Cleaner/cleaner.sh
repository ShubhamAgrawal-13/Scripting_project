#!/bin/bash

#Directory Cleaner

filepath=$1
IFS='
'

if [ ! -d "$filepath" ]; then
	echo "Error : Directory not Found"
	exit
fi

if [ "$2" = "all" ]; then
	files=$(ls "$filepath")
	for file in $files
	do
		#echo $file
		if [ -d "$file" ] ; then
		    echo -n ""
		else
		    fileExt=$( echo "$file" | sed 's/.*\.//' )
		    #echo $fileExt
		    if [ "$file" != "$fileExt" ]; then 
			    direc=$(echo "$filepath/$fileExt")
			    #echo $direc
			    if [ ! -d "$direc" ]; then
				  	mkdir $direc
				fi
				absfile=$(echo "$filepath/$file")
				#echo $absfile
				mv "$absfile" "$direc"
		    fi
		fi
	done
else
	for v in "$@"
	do
		#echo "$v "
		if [ "$1" != "$v" ]; then
			direc=$(echo "$filepath/$v")
			#echo $direc
			if [ ! -d "$direc" ]; then
			  	mkdir $direc
			fi
		fi
	done
	files=$(ls "$filepath")
	for file in $files
	do
		#echo $file
		if [ -d "$file" ] ; then
		    echo -n ""
		else
			fileExt=$( echo "$file" | sed 's/.*\.//' )
			#echo $fileExt
			if [ "$file" != "$fileExt" ]; then 
				direc=$(echo "$filepath/$fileExt")
				#echo $direc
				if [ -d "$direc" ]; then
					absfile=$(echo "$filepath/$file")
					#echo $absfile
					mv "$absfile" "$direc"
				fi
			fi
		fi
	done
fi

echo "Cleaning Completed"

