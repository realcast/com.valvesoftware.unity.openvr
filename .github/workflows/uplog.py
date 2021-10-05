import os
import datetime as dt
import fileinput

Log = open('log.txt','r+')
secondeloop = False
firstloop = False
commit = ""
for line in Log:
    if secondeloop :
        commit = commit + "-" +line
        secondeloop = False
    if firstloop :
        secondeloop = True
        firstloop = False
    if 'Date' in line :
        firstloop = True
Log.close()
os.remove('log.txt')
if 'VER' in os.environ:
    ver = os.environ['VER']
#    repository = os.environ['repository']
    date = dt.datetime.now()
    Date = date.strftime("%d-%B-%Y")
    print("tata")
    with open('package/CHANGELOG.md', 'r') as read_obj, open('package/dummy_file.md', 'w') as write_obj:
        for line in read_obj:
            if '[Semantic Versioning]' in line :
                write_obj.write(line)
                write_obj.write("\n## [")
                write_obj.write(ver)
                write_obj.write("] - ")
                write_obj.write(Date)
                write_obj.write(" : \n")
                write_obj.write(commit)
            else :
                write_obj.write(line)
    print("toto")
    os.remove('package/CHANGELOG.md')
    print("titi")
    os.rename('package/dummy_file.md', 'package/CHANGELOG.md')
    print("tutu")

# This script updates the file CHANGELOG.md by adding all the commits made on
# the branch use to start this workflow
