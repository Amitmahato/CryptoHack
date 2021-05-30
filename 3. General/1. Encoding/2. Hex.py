#! /usr/bin/env python3

# [INFO]
# encrypting something into a ciphertext, the ciphertext has representation in bytes which are not printable ASCII characters
# hence the bytes are converted to hex which is portable accross different systems and can be shared
# lastly the hex values can be converted back to bytes and the ASCII characters can be extracted from them
# which is user friendly and readable 

# given is the hex value of the flag required to solve this challenge, we need to decode it to extract ASCII value to get flag
# hexValue = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
hexValue = "666c6f7765725f6164696461735f736572756d"

# convert hex value to bytes
bytesObj = bytes.fromhex(hexValue) 

# decode the bytes to ASCII
flagInASCII = bytesObj.decode("ASCII")

print("The flag is : ",flagInASCII)