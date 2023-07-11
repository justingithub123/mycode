#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   For - Using a file's lines as a source for the for-loop"""

with open("dnsservers.txt") as dnsfile:
    dnslist = dnsfile.readlines()
    for svr in dnslist:
        print(svr, end="")
