#!/usr/bin/env python3
## Moving files with SFTP

## import paramiko so we can talk SSH
import paramiko
import os

while True:
    con = input("Do you want to continue? Y/n ")
    if con.lower() == "n":
        break
    try:
        where = input("What IP should we connect to? ")
        ## where to connect to
        t = paramiko.Transport(where, 22) ## IP and port
        
        uname = input("What username to use: ")
        pss = input("What is the password? ")
        ## how to connect (see other labs on using id_rsa private/public keypairs)
        t.connect(username=uname, password=pss)
        
        ## Make an sftp connection object
        sftp = paramiko.SFTPClient.from_transport(t)
        
        ## iterate across the files within directory
        for x in os.listdir("/home/student/filestocopy/"): # iterate on directory contents
          if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything that is NOT a directory
            sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x) # move file to target location
        
        ## close the connection
        sftp.close() # close the connection
    except KeyboardInterrupt as err:
        print("\nThanks for using the sftpmover, hope you enjoyed")
        break

print("You have exited the loop")
 
