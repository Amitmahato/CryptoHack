#! /usr/bin/env python3

# [INFO]
# Cryptosystems like RSA works on numbers but our messages are made up of characters.
# How to convert them to numbers so that mathematical operations can be done on them?

# Most common way to achieve it is to take the ordinal bytes of message, convert each (ASCII) to hexademical 
# and concatenate. This can be then represented in either base-16 (hexadecimal) or base-10 (decimal)

# Example: 
# message: HELLO
# ascii bytes: [72, 69, 76, 76, 79]
# hex bytes: [0x48, 0x45, 0x4c, 0x4c, 0x4f]
# base-16: 0x48454c4c4f     (hexadecimal representation)
# base-10: 310400273487a    (decimal representation)

# pip3 install pycryptodome and then import them from Crypto
from Crypto.Util import number

# base-10 (decimal)
longInt = "11515195063862318899931685488813747395775516287289682636499965282714637259206269"

# convert base-10 to base64
flagInBytes = number.long_to_bytes(longInt)
print(help(number))
print(number.tobytes("0x7573635f7265666f726d735f7472656173757265").decode("ASCII"))

# decode the bytes (base64) to ASCII
flagInASCII = flagInBytes.decode("ASCII")

print("The flag is : ",flagInASCII)