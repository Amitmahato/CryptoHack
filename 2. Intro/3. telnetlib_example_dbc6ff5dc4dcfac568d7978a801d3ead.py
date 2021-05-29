#!/usr/bin/env python3

# challenge 3; running this python script will request for the flag on socket.cryptohack.org server on port 11112 
# and print a flag to solve this challenge; this is a sample python script to demonstrate how to make network connection
# and make request and read the received response
# the server socket.cryptohack.org, always uses json to recive request and send response for consistency

import telnetlib
import json

HOST = "socket.cryptohack.org"
PORT = 11112

tn = telnetlib.Telnet(HOST, PORT)


def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)


print(readline())
print(readline())
print(readline())
print(readline())


request = {
    "buy": "flag"
}
json_send(request)

response = json_recv()

print(response)
