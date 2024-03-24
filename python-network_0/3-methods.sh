#!/bin/bash
# Send an OPTION request to the specified URL and display the allowed methods
curl -sI -X OPTIONS "$1" | grep -i Allow | cut -d' ' -f2-
