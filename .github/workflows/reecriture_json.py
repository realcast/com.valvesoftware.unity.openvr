import json
import os
import fileinput

repository = os.environ['repository']
New_ver = os.environ['VER']
with open('Assets/'+repository+'/package.json', 'r') as jsonFile:
    data = json.load(jsonFile)
data['version'] = New_ver
jsonFile = open('Assets/'+repository+'/package.json', 'w+')
jsonFile.write(json.dumps(data, indent=2))
jsonFile.close()

# This script change inside the file package.json the version number.
