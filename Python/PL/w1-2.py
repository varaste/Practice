'''
Write a Python program to get the Python version you are using.

A string containing the version number of the Python interpreter plus additional 
information on the build number and compiler used. 
This string is displayed when the interactive interpreter is started.
'''

import sys
print("Phtyon version is: " + "\n" +sys.version)
print("Version info: ")
print(sys.version_info)