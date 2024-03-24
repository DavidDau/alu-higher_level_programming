#!/usr/bin/python3
"""
This script retrieves the status of the intranet.hbtn.io
website by making an HTTP GET request
and prints details about the response body.
"""

import urllib.request

if __name__ == '__main__':
    # The URL of the intranet.hbtn.io website to check its status
    url = 'https://alu-intranet.hbtn.io/status'

    # Send a request to the URL and read the response
    with urllib.request.urlopen(url) as response:
        # Read the content of the response
        content = response.read()

        # Decode the content to utf-8
        utf8_content = content.decode("utf-8")

        # Print details about the response body
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(utf8_content))
