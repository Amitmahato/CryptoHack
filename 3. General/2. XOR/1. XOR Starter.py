#! /usr/bin/env python3

# XOR works at bit level hence it integers should be converted to binary using bin but python does it implicitly
# syntax: int1 ^ int2 ; ^ is the XOR operator

message = "label"
integer = 13
flag = ""

for char in message:
  flag += chr(ord(char)^integer)

print("The flag is : crypto{"+flag+"}")