#!/bin/bash

copy_text_files () {
  cp $1*.txt $2
}

copy_text_files "$1" "$2"
exit 0