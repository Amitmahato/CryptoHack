#! /usr/bin/env python3

# [INFO]
# from the given list of integers convert them to corresponding ASCII values to generate the flag
# the ASCII is a 7-bit encoding standard and hence allows representation from integer values of 0 to 127 

challengeIntegers = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
correspondingASCII = ""

for integer in challengeIntegers:
  correspondingASCII += chr(integer) # this will generate the corresponding ASCII value from the given integer

print("The flage is : ",correspondingASCII)