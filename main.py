#!/usr/bin/env python
import sys
import base64

args=sys.argv
#print 'Argument List:', str(args)

#check case of arguments
def main(argv):
    action=''
    encoding=''
    string=''

    for arg in argv:
        if arg=="?":
            print 'Usage: main.py -e -a <string>'
            sys.exit()
        elif arg in ("-e", "--encode"):
            #encode
            action='e'
        elif arg in ("-d", "--decode"):
            #decode
            action='d'
        elif arg in ("-a", "--all"):
            #decode/encode with all
            encoding='all'
        elif arg in ("-b64", "--base64"):
            encoding='base64'
        elif arg in ("-u", "--utf8"):
            encoding='utf8'
        #elif arg in ("-:", "--:"):
            #print "Notice:",arg,"is an invalid argument"
        else:
            string=arg

    if action=='e':
        print encode(encoding,string)
    if action=='d':
        print decode(encoding,string)

def encode(encoding,string):
    if encoding in ('base64', "all"):
        return base64.b64encode(string)
    if encoding in ('utf8', "all"):
        return string.encode("ascii")
def decode(encoding,string):
    if encoding in('base64',"all"):
        return base64.b64decode(string)
    if encoding in ('utf8', "all"):
        return string.decode("utf-8", "ignore")

if __name__ == "__main__":
   main(sys.argv[1:])