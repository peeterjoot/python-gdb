from __future__ import with_statement
import gdb
import ebcdic
import codecs

# Prereqs:
#
# sudo yum install python-pip
# sudo pip install ebcdic
# 
# within gdb:
#    (gdb) source -v ~/workspace/python-gdb/ascii.py
#    (gdb) ascii ...
#
class AsciiCommand (gdb.Command):
    """Ascii converts EBCDIC strings to ASCII."""

    def __init__ (self):
        super (AsciiCommand, self).__init__ ("ascii",
                                             gdb.COMMAND_DATA,
                                             gdb.COMPLETE_SYMBOL, True)

    def invoke (self, arg, from_tty):
        print 'EBCDIC: ', arg

        v = gdb.parse_and_eval( arg )
        w = gdb.Value.string( v )
        #v = gdb.selected_frame().read_var( arg )
        #top = gdb.newest_frame()
        #v = top.read_var(arg)
        print 'v: ', arg, ', ', v
        print 'w: ', arg, ', ', w
        d = codecs.decode(w, 'cp1047')
        print 'converted.'
        print 'ASCII: "',d,'"'

AsciiCommand ()
