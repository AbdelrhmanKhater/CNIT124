#!/bin/bash
if [ "$1" == "" ]
then 
echo "Please, Enter 3 numbers such x.x.x"
else
for x in $(seq 1 254); do
ping -c 1 $1.$x | grep -i "64 bytes" | cut -d ' ' -f 4 | sed 's/://'
done
fi
