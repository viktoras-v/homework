#!/bin/bash

# Functions
greet_function () {
                   current_hour=$(date +%H)

                   if [ "$current_hour" -gt "5" ] && [ "$current_hour" -lt "12" ]; then
                    part_of_day="morning"
                   fi

                   if [ "$current_hour" -gt "12" ] && [ "$current_hour" -lt "17" ]; then
                    part_of_day="afternoon"
                   fi

                   if [ "$current_hour" -gt "17" ] && [ "$current_hour" -lt "21" ]; then
                    part_of_day="evening"
                   else
                    part_of_day="night"
                   fi

                   echo "Good$part_of_day $1 "
                   echo "Today is `date +%y%m%d`"
                   echo "Local time is `date +%H`:`date +%M`"
                  }

# Main
if [ ! -n "$1" ]; then
 echo "ERROR! Please provide your name as argument. Example: greet_function.sh Jonas"
 exit 1
fi

greet_function "$1"

exit 0