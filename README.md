# slack-dm

A Python utility to bulk DM users in a Slack workspace by calling the Slack API via HTML requests.

## Prerequisites

This script uses **Python 3** due to its calling of the `print()` method. The script also uses the Python libraries `time` and `requests` to set timeouts and perform HTML GET requests. Run `pip install` as necessary.

To run the script, you'll need a file `users.txt` with the usernames you wish to DM on a separate line, starting at line 1. You can do this by calling the `users.list` method from the Slack API. A simple way to manually generate a `users` file can be done as follows.

## Usage

### Generating a `users.txt` file

1. Visit [https://api.slack.com/custom-integrations/legacy-tokens](https://api.slack.com/custom-integrations/legacy-tokens) to provision a _legacy token_ for the script. Copy and save the token somewhere. 
2. Run `python3 fetch-users.py` to fetch a JSON user directory to the file `users.txt`.

3. Edit the list as necessary such that it contains only usernames of the people to whom messages will be sent.  

### Editing and running `slack-dm.py`

1. On line 6, intialise `token` as a string containing the legacy token.

2. On line 8, edit the list `msgs` to contain any number of messages to be sent. 

	**NOTE:** All messages must be formatted with percent-encoding, ie. all spaces and non-alphanumeric symbols need to be escaped with a percent code.

3. On line 13, initialise `user` as the sending user's (your) username.

4. On line 19, change the sleep variable as necessary.

5. Run `python3 slack-dm.py`. 

6. ???

7. Profit.
