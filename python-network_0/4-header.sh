#!/bin/bash
# Send a GET request to the specified URL with a custom header and display the body of the reponse.
curl -sG -X GET "$1" -H "X-HolbertonSchool-User-Id: 98"
