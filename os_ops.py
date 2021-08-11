#!/usr/bin/env python3
#!/usr/bin/python

import os
import shutil

shutil.copy("movedfile.txt", "example1.txt") 

os.chdir("/home/student")
shutil.copy("myprintedinfo", "copiedfile.txt")
