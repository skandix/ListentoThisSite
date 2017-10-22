#!/bin/sh
source $HOME/.virtualenvs/listen/bin/activate
screen -dmS listen python /opt/ListentoThisSite/server.py
