import os

repository = os.environ['GITHUB_REPOSITORY']
repository=repository.split("/")
print ("::set-output name=rep::"+repository[1])

# This script uses a predefined environmental variable to access the
# repository name.
