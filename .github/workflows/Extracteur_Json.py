import json
import os
import fileinput

repository = os.environ['repository']
Json = open('package/package.json','r')
data = (json.load(Json))
ver = data['version']
print ("::set-output name=Ver::"+ver)
Json.close()

# This script go searches inside the file package.json the current version
# number and set it at an environmental variable.
