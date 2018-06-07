#! /bin/bash

# This script will pull a users file from a given Slack workspace using HTML GET requests.

URL= 		# Add URL for users.list method.

curl $URL -o users 


