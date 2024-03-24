#!/usr/bin/python3
"""
This script sends an HTTP POST request to a specified
URL with a query parameter 'q' containing user-provided input.
It processes the response and prints relevant information.
"""

import requests
import sys

if __name__ == '__main__':
    try:
        """
        Get the user-provided input (query parameter)
        from the command line argument
        """
        params = sys.argv[1]
    except IndexError:
        # If no input provided, set params to an empty string
        params = ""

    # Send an HTTP POST request with the query parameter 'q'
    response = requests.post(
        "http://0.0.0.0:5000/search_user",
        data={"q": params}
    )

    try:
        # Attempt to parse the response as JSON
        json_response = response.json()

        # Check if the response content type is JSON
        if response.headers.get("Content-Type") == 'application/json':
            if len(json_response) > 0:
                # Print user information if available
                print("[{}] {}".format(
                    json_response["id"],
                    json_response["name"])
                )
            else:
                # Print a message if no result found
                print("No result")
    except ValueError:
        # Print an error message if the response is not valid JSON
        print("Not a valid JSON")
