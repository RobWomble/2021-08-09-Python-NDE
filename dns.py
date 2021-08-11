#!/usr/bin/env python3
# open file in read mode
dnsfile = open("dnsservers.txt", "r")
# create list of lines
dnslist = dnsfile.readlines()
# loop over lines
print(dnslist)
for svr in dnslist:
    #print and end without a newline
    print(svr, end="")
    svr = svr.strip()
    print(svr)
# close your file
dnsfile.close()

