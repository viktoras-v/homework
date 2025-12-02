\#!/bin/bash



read -p "Please enter one letter " LETTER



**# Safety**

case $LETTER in

&nbsp;       \[A-Za-z])

&nbsp;           ;;

&nbsp;       \*)

&nbsp;           echo "It is not a letter"; exit 1

&nbsp;           ;;



esac



**# Identify letter**

case $LETTER in

&nbsp;   A|E|I|O|U|Y|a|e|i|o|u|y)

&nbsp;       echo "Your letter $LETTER is vowel"

&nbsp;       ;;

&nbsp;   \*)

&nbsp;       echo "Your letter $LETTER is consonant"

esac



exit 0

