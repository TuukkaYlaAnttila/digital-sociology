#!/bin/bash
# this fixes encoding errors in UTF-8 text files in a very crude way:
# it converts them to LATIN1, transliterating any characters it cannot
# represent in LATIN1, then converts it back to UTF-8. your files will
# not be the same to a computer but they will be human-readable.
#
# give input folder when running: tya-fixencoding.sh folder/
#
# NOTE that this edits files in place, so HAVE A BACKUP

files=$(find $1 -type f)

for eachfile in $files
do
	if file $eachfile | grep -q "ERROR"
		then
			iconv -f UTF-8 -t LATIN1//TRANSLIT $eachfile > $eachfile.1
			iconv -f LATIN1 -t UTF-8 $eachfile.1 > $eachfile
			rm -rf $eachfile.1
			echo "error found and fixed in $eachfile" 
	fi
done