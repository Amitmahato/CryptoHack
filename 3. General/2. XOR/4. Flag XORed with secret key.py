#! /usr/bin/env python3

from pwn import xor

encoded = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
encodedByte = bytes.fromhex(encoded)

# since the flag is in the format crypto{flag here}
# 'crypto{' should have been XORed with secret key (to be found first)
# to get the encoded bytes

# from hit and trial it was found that secret has corresponding value to crypto{ as myXORke 
# and some more part of secret was myXORke+y and making sense of it secret should have to be myXORkey
foundSecret = xor('crypto{',encodedByte).decode("ASCII")[:7] + 'y'
print("SECRET : ",foundSecret)

# now XORing singleByte with the encoded value converted to Bytes
flag = xor(foundSecret,encodedByte).decode("ASCII")

print("The flag is : ",flag)
