#!/usr/bin/env python3

from requests import *
import sys

#
# Usage
#
if len(sys.argv) < 2:
    print('Usage: ./app.py <proxy list file>')
    sys.exit()

HOST = 'https://api.ipify.org'
PROXIES_FILE = sys.argv[1]

proxy = dict()

with open(PROXIES_FILE) as file:
    for line in file:

        # If the current line starts with a # or it's empty, pass the line
        if line[0] == '#' or line == "\n":
            continue

        # Remove line break character and split the current line in diferent parts
        line_parts = line.replace('\n', '').split(':')

        # Build a proxy url and put it inside a dictionary
        proxy['https'] = f'{line_parts[0]}://{line_parts[1]}:{line_parts[2]}'

        # Try to send a request
        try:

            r = get(HOST, proxies=proxy, timeout=7)

            print(f"{proxy['https']} - successfull")
        except:
            pass
