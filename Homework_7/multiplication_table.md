\#!/bin/bash



**#Variables**

read -p "Enter number from 1 to 10 " NUMBER



**#Main**



while \[ "$NUMBER" -lt 1 ] || \[ "$NUMBER" -gt 10 ]; do

&nbsp;	read -p "Please, enter number between 1 and 10 " NUMBER

done



for i in {1..10}; do

&nbsp;	echo $NUMBER x $i = $(($NUMBER \* $i))

done



exit 0

