#!/bin/bash 
# take in a url and displays the size of the body of the response 
curl -sI "$1" | grep 'Content-Length'| cut -d " " -f2
