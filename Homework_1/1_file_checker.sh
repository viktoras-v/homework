#/!bin/bash

check_file () {
  if [ -r $1 ]; then
    echo "File $1 is readable"
  fi
  if [ -w $1 ]; then
    echo "File $1 is writable"
  fi
  if [ -x $1 ]; then
    echo "File $1 is executable"
  fi
}

check_file /etc/passwd

exit 0
