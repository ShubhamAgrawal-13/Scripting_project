#!/bin/bash

#Password
echo -n "Enter Password : "
stty -echo
read pass
stty echo
echo ""
#echo $pass

plen=`echo -n $pass | wc -m`

num=$(echo "$pass" | grep -E "[0-9]")
spe=$(echo "$pass" | grep -E "[@#$%&%*-+=]")

#echo "$len $num $spe"

if [ "$pass" != "$num" -o "$pass" != "$spe" -o $plen -lt 8 ]; then
	 echo -n "Weak Password : "
	 if [ $plen -lt 8 ]; then 
	 	echo -n " ***less than Minimun length(8)*** "
	 fi
	 if [ "$pass" != "$num" ]; then 
	 	echo -n " ***No number*** "
	 fi
	 if [ "$pass" != "$spe" ]; then 
	 	echo -n " ***No special character*** "
	 fi
	 echo ""
	 exit
fi

plen=`echo -n $pass | wc -m`

for((i=4;i<=plen;i++))
do
	for((j=0;j<plen;j++))
	do
		if ((i+j>plen))
		then
			break
		fi
		a=${pass:$j:$i}
		
		# aa="$a"
		ll=$(grep -ic "^$a$" /usr/share/dict/words)
		lll=$(grep -i "^$a$" /usr/share/dict/words)
		#ll=$(grep "^.*$" /usr/share/dict/words | grep -ic "$a")
		#lll=$(grep "^.*$" /usr/share/dict/words | grep -i "$a")
		if [ $ll -ge 1 ];
		then
			# echo "$a----------------"
			# for lf in $lll:
			# do
			# 	echo "$lf"
			# done
			echo "Weak Password : Contains some dictionary word(s)"
	 		exit
		fi
	done
done

echo "Strong Password "




