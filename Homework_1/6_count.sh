#!/bin/bash

count () {
  ls -lar $1 | wc -l
}

count "$1"

exit 0
