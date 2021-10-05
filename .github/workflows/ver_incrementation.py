import os

version = os.environ['ver']
versionsplit = version.split(".")
versionsplit[2]=str(int(versionsplit[2])+1)
VER = ""
for i in range(0,2) :
    VER = VER + versionsplit[i]
    VER = VER + "."
VER = VER + versionsplit[2]
print ("::set-output name=VER::"+VER)

# This script increment the last digit of the version number take
# in file package.json
