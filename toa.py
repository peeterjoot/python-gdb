#!/usr/bin/python

import ebcdic
import codecs
import gdb

class AsciiPrefixCommand (gdb.Command):
    "EBCDIC to ASCII string conversion."

    def __init__ (self):
        super (AsciiPrefixCommand, self).__init__ ("ascii",
                                                  gdb.COMMAND_SUPPORT,
                                                  gdb.COMPLETE_NONE, True)

    AsciiPrefixCommand()

#for a in args:
#    print 'arg: ', a
#    print 'arg: ', codecs.decode(a, 'cp1047')

#with io.open('myfile.txt', 'r', encoding="cp500") as fh:
#for line in fh:
#data = json.loads(line)
