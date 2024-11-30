#!/usr/bin/python3
"""
takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
import sys

def search_user(letter=""):
    url = "http://0.0.0.0:5000/search_user"
    
    # Send the POST request with the letter as the query parameter
    response = requests.post(url, data={'q': letter})
    
    try:
        # Attempt to parse the JSON response
        response_json = response.json()
        
        if response_json:
            # If the response is not empty, display the id and name
            print(f"[{response_json.get('id')}] {response_json.get('name')}")
        else:
            # If the response is empty, display 'No result'
            print("No result")
    
    except ValueError:
        # If JSON is invalid, display 'Not a valid JSON'
        print("Not a valid JSON")

if __name__ == "__main__":
    # If there's a command-line argument, use it as the letter
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    
    # Call the search_user function with the letter
    search_user(letter)

