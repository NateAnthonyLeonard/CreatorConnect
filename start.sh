#!/bin/bash

# server start script
# at least for backend lol
# TODO: Add proper SSL support

# disclaimer
echo "THIS SCRIPT WILL ONLY WORK ON OUR DEVELOPMENT SERVER"
echo "IF YOU'RE GETTING ERRORS RUNNING THIS ON YOUR RIG, YOU HAVE BEEN WARNED"

# key locations
CERT_FILE=/etc/letsencrypt/live/canipleasegetsome.space/cert.pem
KEY_FILE=/etc/letsencrypt/live/canipleasegetsome.space/privkey.pem

# prepare logging
LOGFILE=server.log
echo Server started at $(date +"%H:%M:%S on %m-%d-%Y.") > $LOGFILE

# other variables we'll want
SESSIONNAME=flaskServer
HOST=0.0.0.0
PORT=80 #443

# # cd into api and prepare
# cd api
# export FLASK_ENV=development
# export FLASK_APP=api_main.py

# Compile website

# Set up virtualization
tmux ls | grep -Fx $SESSIONNAME
if [ $? != 0 ]; then
    echo "Existing session found! Killing..."
    tmux kill-session -t $SESSIONNAME
fi

# run server
echo "Starting new server instance..."
tmux new-session -d -s $SESSIONNAME flask run --host $HOST --port $PORT > $LOGFILE
echo "Server started! Visit the page to run a test!"