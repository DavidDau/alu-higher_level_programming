#!/usr/bin/python3
"""
This script retrieves the status of the intranet.hbtn.io
website using the requests library
and prints details about the response content.
"""

import requests

if __name__ == '__main__':
    # Send an HTTP GET request to the specified URL
    response = requests.get('https://alu-intranet.hbtn.io/status')

    # Print details about the response body
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
