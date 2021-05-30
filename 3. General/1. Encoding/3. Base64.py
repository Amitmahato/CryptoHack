#! /usr/bin/env python3

# [INFO]
# Base64 - another encoding scheme allowing us to represent binary data into ASCII string of 64 characterss 
# 6 bits = 1 character of base64
# .`. .'. .^. Therefore
# 3 bytes = 3 * 8 bits = 24 bits = 24/6 = 4 base64 characters

# base64 is most commonly used online, where binary data such as images can be easily included in HTML or CSS files 

import base64

# given is the hex value of the flag required to solve this challenge
# we need to decode it to bytes and encode to base64 (represented by wrapping with b'' around) 
# and extract ASCII value (to remove b'' wrapping from flag) to get flag
hexValue = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# convert hex value to bytes
bytesObj = bytes.fromhex(hexValue) 

# encode the bytes to base64
flagInBase64 = base64.b64encode(bytesObj)

# this is from one of the level level in Encoding challenge
# flagInBase64 = base64.b64decode("ZHJhbWF0aWNfc3Vic2NyaXB0aW9uX2Nsb3VkeQ==")

# decode the bytes to ASCII for the flag
flagInASCII = flagInBase64.decode("ASCII")

print("The flag is : ",flagInASCII)