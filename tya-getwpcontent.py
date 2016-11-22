#coding=UTF-8
# get entry titles and content from wordpress html files
#
# finds all h2 elements of class entry-title and div
# elements of class entry-content and writes them in
# the same folder as the original but with -output.html
# suffix
#
# run in a folder containing html files that are wordpress posts
#
# tuukka.yla.anttila@gmail.com 22 Nov 2016

from bs4 import BeautifulSoup
import re
import argparse
import lxml
from string import maketrans
import os
import sys
import glob
import codecs

filenamelist = glob.glob('*.html')

for filename in filenamelist:
    soup = BeautifulSoup(open(filename), "html.parser")
    otsikko = soup.find_all('h2', class_='entry-title')
    sisalto = soup.find_all('div', class_='entry-content')
    newfilename = '%s-output.html' % filename
    for otsikkoinstance in otsikko:
        print otsikkoinstance
        out = open(newfilename,'a')
        out.write(str(otsikkoinstance))
        out.close() 
    for sisaltoinstance in sisalto:
        print sisaltoinstance
        out = open(newfilename,'a')
        out.write(str(sisaltoinstance))
        out.close()
        
        