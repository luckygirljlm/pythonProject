#!/usr/bin/env python
#coding: utf-8

import re
import urllib2 as myurl
import sys

newFilms = []
bestFilmsThisWeek = []
filmsInNorthUSA = []
def parsePage(targetUrl, targetFileName):
    s = myurl.urlopen(targetUrl)
    content = s.read()
    parseNewFilms(content)
    #parseBestFilmsThisWeek(content)
    #parseFilmsInNorthUSA(content)
    
def parseNewFilms(content):
    try:
        pattern = re.compile(r'<table width="100%" class="">.*?</table>', re.S)
        matches = pattern.findall(content)   
        if matches:     
            for item in matches:                     
                subPattern = re.compile(r'<a class="nbg" href=.*?</a>', re.S)
                results = subPattern.findall(item)
                if results:
                    url = results[0].split('href="')[1].split('"')[0]
                    title = results[0].split('title="')[1].split('">')[0].decode('utf-8')
                    img = results[0].split('src="')[1].split('"')[0]
                    print url,title,img,
                date = item.split('class="pl">')[1].split('(')[0]
                area = item.split('class="pl">')[1].split('(')[1].split(')')[0].decode('utf-8')
                if len(item.split('class="rating_nums">')) > 1:
                    stars = item.split('class="rating_nums">')[1].split('<')[0]
                else:
                    stars = "尚未上映".decode('utf-8')
                print date,area,stars
                newFilms.append((title,url,img,date,stars))
    except e:
        print '!!!!!!!!!!!!!!!!error occur in Function parseNewFilms:',e                              
         
   




def usage():
    print 'run "python ./worm.py -help": how to use the current script'
    print 'run "python ./worm.py targetUrl targetFilName": parse targetUrl and save the result to file named targetFileName'


if __name__ == '__main__':    
    if len(sys.argv) == 2 and sys.argv[1] == '-help':
        usage()
        sys.exit()
    elif len(sys.argv) == 3:
        parsePage(sys.argv[1], sys.argv[2])
    else:
        print 'please give correct parameters following rules'
        usage()
        sys.exit()         
            
            
