#!/bin/bash
#Snake game
len=25
rw=2
cl=2
width=$(($(tput lines)-rw)) 
height=$(($(tput cols)-cw))
x=$(echo `expr $width / 2`)
y=$(echo `expr $height / 2`)
game=1
k=0
move=0
for((i=0;i<len;i++))
do
	((xx[i]=x))
	((yy[i]=y-i-1))
done

((px=xx[len-1]))
((py=yy[len-1]))

arrow_up="^"
arrow_down="v"
arrow_left="<"
arrow_right=">"
space=" "

function printBoard()
{
	clear
	#echo "*********************** Snake Game  **************************"
	for ((i=1; i<=width; i++)); do
	   for ((j=1; j<=height; j++)); do
	   		if [ $i -eq 1 -o $i -eq $width -o $j -eq 1 -o $j -eq $height ]; then
			       echo -n "*"
			else
				if [ $i -eq $x -a $j -eq $y ]; then
	               #echo -n ">"
	               #tput cup $x $y
	    		   #echo "O"
					echo -n " "
	            else
	               echo -n " "
	            fi
			fi
	   done
	   echo ""
	done
	echo " * Press any directionals key to start game or to move snake *   To Quit: press q "
}

echo "Press any key to start the game"
read -N 1 direc
move=4
printBoard


#echo $x $y
stty -echo
while [ 1 ] ; 
do
	    #echo "$c"
	    tput civis
	    read -t 0.15 -N 1 c

	    # To detect arrow keys
	    if [ "$c" = 'A' ]; then
	    		move=1          #up
	    elif [ "$c" = 'B' ]; then
	    		move=2         #down
	    elif [ "$c" = 'D' ]; then
	    		move=3           #left
	    elif [ "$c" = 'C' ]; then
	    		move=4           #right
	    elif [ "$c" = "" ]; then
	    		move=$move           
	    elif [ "$c" = "q" ]; then
	    	game=1
	    	# ((x=1))
		    # ((y=height-2))
		    # tput cup $x $y
		    # echo ""
	    	break
	    fi
	    tput cup $px $py
	    echo "$space"
	    if [ "$move" = "1" ]; then
	    		((x=x-1))          #up
	    		co=`tput setaf 4`
				echo "${co}${NC}"
	    		tput cup $x $y
	    		echo "$arrow_up"
	    elif [ "$move" = "2" ]; then
	    		((x=x+1))           #down
	    		co=`tput setaf 3`
				echo "${co}${NC}"
	    		tput cup $x $y
	    		echo "$arrow_down"
	    elif [ "$move" = "3" ]; then
	    		((y=y-1))           #left
	    		co=`tput setaf 1`
				echo "${co}${NC}"
	    		tput cup $x $y
	    		echo "$arrow_left"
	    elif [ "$move" = "4" ]; then
	    		((y=y+1))			#right
	    		co=`tput setaf 2`
				echo "${co}${NC}"
	    		tput cup $x $y
	    		echo "$arrow_right"
	    fi
	    ((px=xx[len-1]))
	    ((py=yy[len-1]))
	    for((i=len-2;i>=0;i--))
	    do
	    	((xx[i+1]=xx[i]))
	    	((yy[i+1]=yy[i]))
	    done
	    ((xx[0]=x))
	    ((yy[0]=y))
	    
	    for((i=1;i<len;i++))
	    do
	    	tput cup ${xx[$i]} ${yy[$i]}
	    	echo "O"
	    done
	    # tput cup $px $py
	    # echo " "
	    if ((x<=0 || x>=width-1 || y<=0 || y>=height-1)); then
		       game=1
		       # ((x=1))
		       # ((y=height-2))
		       # tput cup $x $y
		       # echo " " 
		       #echo "hello"
		 	   break
		fi
	    # stty echo
	    #printBoard
	    #echo "--------------$c--------------"
	    sleep 0.11
done
stty echo
clear

echo "Game Over"




