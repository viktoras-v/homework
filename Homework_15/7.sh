#!/bin/bash

# Script to edit student Antanas age

# Function to read current age
read_age () {
  age=$(jq .student.age $filename)
  echo "Age of Antanas is $age"
}



# Input json filename
read -p "Enter filename: " filename
if [ ! -w $filename ]; then 
  echo "File not exists or not writable"; 
  exit 126;
fi

# Read current age
read_age


# Write new age
read -p "Enter new age: " age
jq --arg age "$age"  '.student.age = ($age | tonumber)' $filename > /tmp/$filename && mv /tmp/$filename $filename


# Read new age
read_age


exit 0



