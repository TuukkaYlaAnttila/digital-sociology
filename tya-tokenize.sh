#!/bin/bash
#
# run from command line: tya-tokenize.sh folder/
#
# NOTE!!! this edits files IN PLACE, so make a backup!
#
# tuukka.yla.anttila@gmail.com 22 November 2016

# get list of files in given folder

find $1 -iname ".*" -type f -delete ;

inputfiles=$(find $1 -type f)

# do stuff to each file

for file in $inputfiles
do
	echo "tokenizing $file"
	
	# turn spaces into newlines
	perl -pe 's/\s+/\n/g' $file > $file.1; mv $file.1 $file
	
	# remove spaces
	sed 's/[[:blank:]]//g' $file > $file.1; mv $file.1 $file
	
	# remove empty lines
	sed '/^\s*$/d' $file > $file.1; mv $file.1 $file
	
	# remove non-alphabet characters
	sed -e 's/[^a-öA-Ö]/ /g;s/  */ /g' $file > $file.1; mv $file.1 $file
	
	# replace spaces with newlines again
	perl -pe 's/\s+/\n/g' $file > $file.1; mv $file.1 $file
	
	# and remove empty lines again
	sed '/^\s*$/d' $file > $file.1; mv $file.1 $file
done