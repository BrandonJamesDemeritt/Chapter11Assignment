'''
Created on Nov 4, 2022

@author: Brandon Demeritt
'''


import zipfile

string = input("Please enter the zip name: ")
z = zipfile.ZipFile(string, "w")

filename = ""
while filename != "quit":
    filename = input("Please enter the filename to zip: ")
    if filename == "quit":
        break
    z.write(filename)
    
print("\nEnd of Line")