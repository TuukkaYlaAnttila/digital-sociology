#!/bin/bash
# look for given string in files in a given folder and give file name if found

files=$(find $1 -type f)

for eachfile in $files
do
	if grep "The Republican Party, as far as public perception is concerned" $eachfile
	then echo $eachfile
	fi	
done