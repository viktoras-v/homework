\#!/bin/bash



**#Variables**

read -p "Enter first multiplier from 1 to 10 " MULTIPLIER\_1

read -p "Enter second multipliеr " MULTIPLIER\_2

count=1

max\_attempt=3



**#Multiplier\_1 safety check**

attempt=0

while \[ "$MULTIPLIER\_1" -lt 1 ] || \[ "$MULTIPLIER\_1" -gt 10 ]; do

&nbsp; read -p "Please, enter number between 1 and 10 " MULTIPLIER\_1

&nbsp; ((attempt++))

\# safety

&nbsp; if \[ $attempt -gt $max\_attempt ]; then

&nbsp;   echo "Error.Too much attempts"

&nbsp;   exit 1

&nbsp; fi

done



**#Multiplier\_2 safety check**

attempt=0

while \[ "$MULTIPLIER\_2" -lt 1 ] || \[ "$MULTIPLIER\_2" -gt 10 ]; do

&nbsp; read -p "Please, enter number between 1 and 10 " MULTIPLIER\_2

&nbsp; ((attempt++))

\# safety

&nbsp; if \[ $attempt -gt $max\_attempt ]; then

&nbsp;   echo "Error.Too much attempts"

&nbsp;   exit 1

&nbsp; fi

done



**#Calculations**

while \[ ! $count -gt  $MULTIPLIER\_2 ]; do

&nbsp;   echo $MULTIPLIER\_1 x $count = $((MULTIPLIER\_1 \* count))

&nbsp;   ((count++))

done



exit 0

