**1. Еssay**

Bash scripting is an interpreted language that is perfect for internal Linux housekeeping tasks, such as system maintenance. 

As I understand it, when it comes to external integrations, Bash is not the best choice. In such cases, it’s worth looking at more powerful languages like Python.



2\. Greetings

\#!/bin/bash

\# Greetings

echo "Hello, World!"

exit 0



*chmod +x hello\_script.sh*



**3. Favourite food**

\#!/bin/bash

\#Variables

NAME="Viktoras"

FOOD="caffeine"

\#Main

echo "My name is $NAME and my favourite food is $FOOD"

exit 0



**4. Modified food**

\#!/bin/bash

\#Variables

NAME="Viktoras"

FOOD="caffeine"

CURRENT\_DATE=$(date)

\#Main

echo "Today is $CURRENT\_DATE. My name is $NAME and my favourite food is $FOOD"

exit 0



**5. Favorite colour**

\#!/bin/bash

\#Variables

read -p "What is your name? " NAME

read -p "What is your favorite color? " COLOR

\#Main

echo "Hello, $NAME. Your favorite color is $COLOR"

exit 0



**6. Table uses printf**

\#!/bin/bash

\# Variables

read -p "What is your name ?" MY\_NAME

read -p "What is your favorite color?" MY\_COLOR

\# Arrays

NAMES=("Gintaras" "Andrius" "$MY\_NAME")

COLORS=("red" "blue" "$MY\_COLOR")

\#Main

for i in {0..2}; do

printf "%s %s\\n" "${NAMES\[$i]}" "${COLORS\[$i]}"

done

exit 0



**7. Math**

\#!/bin/bash

\#Variables

read -p "Enter first number " FIRST\_NUMBER

read -p "Enter second number " SECOND\_NUMBER

\#Main

echo $((FIRST\_NUMBER + SECOND\_NUMBER))

echo $((FIRST\_NUMBER - SECOND\_NUMBER))

echo $((FIRST\_NUMBER \* SECOND\_NUMBER))

echo $((FIRST\_NUMBER / SECOND\_NUMBER))

exit 0

