#!/usr/bin/python

import sys
import ebcdic
import codecs

args = sys.argv
del args[0]

for a in args:
    print 'arg: ', a
    print 'arg: ', codecs.decode(a, 'cp1047')

#with io.open('myfile.txt', 'r', encoding="cp500") as fh:
#for line in fh:
#data = json.loads(line)
