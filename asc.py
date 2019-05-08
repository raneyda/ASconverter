#!/usr/bin/python3

#
#   Imports
#
import sys
import math

#
#   Functions
#
def getopts(argv):
    if len(sys.argv) > 1:
        return argv[1]
    else:
        print("No arguments given")
        exit()

def bitLen(int_type):
    length = 0
    while (int_type):
        int_type >>= 1
        length += 1
    return(length)

def asplain():
    return

def asdot():
    return

def asdotplus():
    return

#
#   Main Program
#
if __name__ == '__main__':

    #
    #   Grab the AS number from the command line
    #
    ASN = int(getopts(sys.argv))
    ASNlen = bitLen(ASN)
    if (ASN > 0): 
        print(bitLen(ASN))
        if (ASNlen <= 16):
            print("Binary: ", '{0:016b}'.format(ASN))
        elif (ASNlen > 16) and (ASNlen <= 32):
            print("Binary: ", '{0:032b}'.format(ASN))
        else:
            print("ASN value is non-negative but not a valid AS number")
            exit()
    else:
        print("AS numbers can't be negative")
        exit()


"""
References:

Autonomous System (AS) Number Reservation for Documentation Use
https://tools.ietf.org/html/rfc5398

Reservation of Last Autonomous System (AS) Numbers
https://tools.ietf.org/html/rfc7300

Textual Representation of Autonomous System (AS) Numbers
https://tools.ietf.org/html/rfc5396

Guidelines for creation, selection, and registration
of an Autonomous System (AS)
https://tools.ietf.org/html/rfc1930

Autonomous System (AS) Reservation for Private Use
https://tools.ietf.org/html/rfc6996

BGP Support for Four-Octet Autonomous System (AS) Number Space
https://tools.ietf.org/html/rfc6793
"""
