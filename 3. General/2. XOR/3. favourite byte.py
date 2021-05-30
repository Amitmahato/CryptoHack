#! /usr/bin/env python3

from pwn import xor

encoded = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
byteObj = bytes.fromhex(encoded)

firstChar = byteObj.decode("ASCII")[0]

# since the flag is in the format crypto{flag here}
# 'c' should have been XORed with single byte (to be found first)
# to get the first character of the decoded output

singleByte = xor(firstChar,'c')

# now XORing singleByte with the encoded value converted to Bytes
flag = xor(singleByte,byteObj).decode("ASCII")

print("The flag is : ",flag)
