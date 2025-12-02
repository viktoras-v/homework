#!/bin/bash

read -p "Provide directory name for backup " DIRECTORY

# Safety check
if [ -z "$DIRECTORY" ]; then
  echo "Error. Directory is empty."; exit 1
fi

# Check if enough space for backup function
check_free_space () {
space_available=$(df --output=avail  /  | awk 'NR==2')
space_required=$(du -shb /etc/ | awk '{print $1}')
if [ "$space_available" -lt "$space_required" ]; then
  echo "Error. Not enough space."; exit 2
fi
}

# Make backup function
make_backup () {
tar -czf backup.tgz $1 2>backup.errors.log
}

# Backup
check_free_space $DIRECTORY
make_backup $DIRECTORY
if [ $? -eq 0 ]; then
  echo "Backup done"
else
  echo "Backup failed"
fi

exit 0
