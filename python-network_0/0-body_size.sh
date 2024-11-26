#!/bin/bash
# This script takes in a URL, sends a request to that URL using curl and displays the size of the body of the response in bytes
curl -so /dev/null -w '%{size_download}\n' $1
