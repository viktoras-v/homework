#!/bin/bash

for number in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ; do

if (( number % 2 == 0 )); then
    echo "Number $number is even"
else
    echo "Number $number is odd"
fi

done

exit 0