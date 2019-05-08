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

def asplain(num):
    ASNhigh, ASNlow = ASNtest.split(".",1)
    #
    #   Validate negative numbers were not used
    #   and convert to asplain
    #
    if (int(ASNhigh) > 0) and (int(ASNlow) > 0): 
        temphigh = '{0:016b}'.format(int(ASNhigh))
        templow = '{0:016b}'.format(int(ASNlow))
        tempASN = int(temphigh+templow,2)
    else:
        print("AS numbers can't be negative")
        exit()

    if (bitLen(tempASN) <= 32) and (tempASN > 0):
        return tempASN
    elif bitLen(tempASN) > 32:
        print("Not a valid ASN - exceeds 4 bytes")
        exit()
    else:
        print("Error occured")
        exit()

def asdot(num):
    if (ASN > 0): 
        ASNlen = bitLen(ASN)
        #print(bitLen(ASN))
        if (ASNlen <= 16):
            return "0." + str(int(ASN))
        elif (ASNlen > 16) and (ASNlen <= 32):
            tempASN = '{0:032b}'.format(ASN)
            high = int(tempASN[:16],2)
            low = int(tempASN[17:],2)
            return str(high) + "." + str(low)
        else:
            print("ASN value is non-negative but not a valid AS number")
            exit()
    else:
        print("AS numbers can't be negative")
        exit()
    
    return

#
#   Main Program
#
if __name__ == '__main__':

    #
    #   Grab the AS number from the command line
    #
    ASNtest = str(getopts(sys.argv))

    #
    #   Determine if input is asdot notation
    #
    ASNresult = ASNtest.find(".")
    if ASNresult >= 1:
        print("Input (asdot):   ", ASNtest, "\nOutput (asplain):", asplain(ASNtest))


    #
    #   Otherwise input is asplain notation
    #
    else:
        ASN = int(ASNtest)
        print("Input (asplain):", ASN, "\nOutput (asdot): ", asdot(ASN))
