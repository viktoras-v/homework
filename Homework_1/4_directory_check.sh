#!/bin/bash

read -p "Enter file or directory " DIR

check_dir () {
  if [ -f "$1" ]; then
    echo "$1 is file"
  fi

  if [ -d "$1" ]; then
    echo "$1 is dir"
  fi
}


check_dir "$DIR"
exit 0