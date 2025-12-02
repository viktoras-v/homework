#!/bin/bash

# Input array
for i in {1..15}; do
    read -p "Input number " list[i]
done

# Iterate through array
for number in ${list[@]} ; do

# Conditional check
if (( number % 2 == 0 )); then
    echo "Number $number is even"
else
    echo "Number $number is odd"
fi

done

exit 0