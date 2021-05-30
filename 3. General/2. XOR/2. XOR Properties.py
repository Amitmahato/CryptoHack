#! /usr/bin/env python3

from pwn import xor

# Given:
# KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313" => K1
# KEY2 ^ KEY1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e" => K21 = K12
# KEY2 ^ KEY3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1" => K23 = K32
# FLAG ^ KEY1 ^ KEY3 ^ KEY2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf" => Flag ^ K1 ^ K23 = finalKey

# Solution:
# flag ^ (KEY1) ^ (KEY3 ^ KEY2) = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"
# flag ^ (K1) ^ (K32) = finalKey
# flag = (K1) ^ (K32) ^ finalKey
# flag = K1 ^ K23 ^ finalKey

# now converting the hex values to bytes and using pwn.xor to find the flaginbyte and then decode it to ASCII

K1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
K23 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
finalKey =  "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

flag = xor(bytes.fromhex(K1),  bytes.fromhex(K23), bytes.fromhex(finalKey)).decode("ASCII")

print("The flag is : ",flag)
