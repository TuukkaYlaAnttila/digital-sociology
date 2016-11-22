#coding=UTF-8
# 
# get post metadata and content from Simple Machines Forum prints
#
# run this in a folder which contains SMF "print thread" html files
# to get EACH POST from the thread as a separate file, named by timestamp,
# thread title and poster nickname. these will be placed in subfolder named
# output. how you get the "print thread" files is your business
#
# NOTE that you need the subfolder named "output" which this script
# does not create
#
# run this like this: python3 tya-getsmfposts.py
#
# note that you will probably need python 3 or 3.5
# ...and BeautifulSoup, and Bleach, and stuff
#
# tuukka.yla.anttila@gmail.com 22 nov 2016

# import needed modules/libraries

from bs4 import BeautifulSoup
import re
import argparse
import lxml
# didn't need this one eh?
#from string import maketrans
import os
import sys
import glob
import codecs
import bleach

# get list of html files in directory
filenamelist = glob.glob('*.html')

# open a file
for filename in filenamelist:
    
    print(filename)
    
    #open file to beautifulsoup
    soup = BeautifulSoup(open(filename), "html.parser")
    
    #get post headers
    postheaders = soup.find_all('dt', class_='postheader')
    
    #get post bodies
    postbodies = soup.find_all('dd', class_='postbody')
    
    #combine them as a list of tuples
    tuples = list(zip(postheaders,postbodies))
    
    # do stuff to each header-body-pair
    for eachtuple in tuples:
        
        #get tuples as strings
        tuplestr = str(eachtuple)

        #get post title
        headersoup = BeautifulSoup(tuplestr, "html.parser")
        title = headersoup.find('strong')
        titlecontents = str(title.contents)
        posttitle = re.sub(r"[^A-Za-z]+", '', titlecontents)
        
        #get author
        nick = title.find_next('strong')
        nickcontents = str(nick.contents)
        postnick = re.sub(r"[^A-Za-z]+", '', nickcontents)
        
        #get timestamp
        time = nick.find_next('strong')
        timecontents = str(time.contents)
        posttime = re.findall('\d+', timecontents)
        fields = len(posttime)
        
        #fix bug in smf which gives midnight hour as blank instead of 00
        if fields < 6:
            posttime.insert(3,'00')
        
        #re-order timestamp
        timeformat = [2,1,0,3,4,5]
        posttime = [ posttime[i] for i in timeformat]
        timestamp = ''.join(posttime)
        
        #get postbody
        bodysoup = BeautifulSoup(tuplestr, "html.parser")
        
        #remove quotes of previous messages and other extra tags
        [s.decompose() for s in bodysoup('div')]
        [s.decompose() for s in bodysoup('blockquote')]
        [s.decompose() for s in bodysoup('br')]
        
        #get and clean postbody
        postbody = bodysoup.find('dd', class_='postbody')
        contents = bleach.clean(postbody, tags=[], strip=True)
        #tyyppi = type(contents)
        #print(tyyppi)
        
        #write postbody to named file
        newfilename = 'output/' + timestamp + '-' + posttitle[0:40] + '-' + postnick[0:10] + '.txt'
        out = codecs.open(newfilename,'a','utf-8')
        out.write(contents)
        out.close()       
        


        