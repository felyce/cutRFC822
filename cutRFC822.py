#!/usr/bin/python
# -*- coding: utf-8; mode: python-mode -*-
# First 2009/6/30.
# Last Change:2009/07/01 00:42:21.

import os
import sys
import re

def _getLastFile():

    x = os.listdir('./')
    y = []

    for f in x:
        if os.path.isfile( os.path.abspath(f) ): 
            if re.match('\d+', f):
                y.append( int(f) )

    y.sort()

    return y[-1]


def _splitMail( _file ):

    x = []
    f = open(_file)
    a = f.read()
    f.close()

    x = re.split('----.+--\nContent-Type: message/rfc822\n\n', a)

#    print x
    return x


def _main():

    file_list = sys.argv[1:]

    last_file_num = _getLastFile()
    emls = []

    for file in file_list:

        print (file)

        emls = _splitMail(file)

        for i in range( len( emls ) ):
            if not emls[i]:
                continue
            
            try:
                """
                start count for 0, so file overwrite.
                + 1, no overwrite.
                """
                f_w = open(str( last_file_num + 1 + i), 'w')
                f_w.write( emls[i] )
                f_w.close()

            except IOError:
                print ("Can't write %d." % last_file_num + i)


if __name__ == '__main__':
    _main()
