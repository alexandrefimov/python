import sys
import os

x = len(sys.argv)
if x > 1:
    if sys.argv[1] == "/?":
        print("Help Requested")
    print("Arguments: " + str(sys.argv[1:]))
else:
    print("Arguments not provided!")

os.system("dir")