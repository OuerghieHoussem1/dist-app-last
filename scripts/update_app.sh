#!/bin/bash
echo Starting update
cd /root/dist-app-last/
git stash
echo Downloading new code
sleep 3

git pull
cd ./scripts

echo Updating permissions
sleep 3

chmod +x *.*

echo Update finished
echo "Restarting in"
echo 3
sleep 1
echo 2
sleep 1
echo 1
sleep 1

reboot