#!/bin/bash
# Make the python script executable
chmod +x $1
# Add the file to git
git add $1
# Update the file permissions in git
git update-index --chmod=+x $1
git commit -m "$2"
git push