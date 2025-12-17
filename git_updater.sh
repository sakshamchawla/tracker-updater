#!/bin/bash
if [ -d "trackerslist/.git" ]; then
    cd trackerslist && git pull
else
    git clone https://github.com/ngosang/trackerslist.git
fi