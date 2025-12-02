#!/bin/bash

read -p "Enter a string " STRING

echo "Converting to uppercase.."
echo $STRING | tr [:lower:] [:upper:]
exit 0