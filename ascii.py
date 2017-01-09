from __future__ import with_statement
import gdb
import ebcdic
import codecs

# Prereqs:
#
# sudo yum install python-pip
# sudo pip install ebcdic
#
class AsciiCommand (gdb.Command):
    """Ascii converts EBCDIC strings to ASCII."""

    def __init__ (self):
        super (AsciiCommand, self).__init__ ("ascii",
                                             gdb.COMMAND_SUPPORT,
                                             gdb.COMPLETE_NONE, True)

    def invoke (self, arg, from_tty):
        print 'EBCDIC: ', arg
        d = codecs.decode(arg, 'cp1047')
        print 'ASCII: ', d

AsciiCommand ()
