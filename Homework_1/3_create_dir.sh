#!/bin/bash

read -p "Enter directory name " DIRECTORY
read -p "Enter file name " FILE

files_creator () {
  mkdir $1
  touch $1/$2
}

files_creator "$DIRECTORY" "$FILE"

exit 0