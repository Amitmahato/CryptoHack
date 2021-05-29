#! /usr/bin/env python3
import sys

def caesarCipher(str, shift):
  str = str.casefold()
  alphabetArr = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ");
  res = "";

  for char in str:
    idx = alphabetArr.index(char);

    if idx == -1:
      res += char;
      continue;

    encodedIdx = (idx + shift) % 26
    res += alphabetArr[encodedIdx]
  return res;

# grab words from arguments sent to this file
seq = sys.argv[1:] or ["RFWD", "HCOGH", "QOBMCB", "GVSR"]

for i in range(26):
  original = ""
  nthRes = ""
  for word in seq:
    original += word.casefold() + " "
    shifted = ""
    for char in word:
      shift = i
      shifted += caesarCipher(char,shift)

    nthRes += shifted + " "
  # find the combination of words from all 26 iteration that makes sense
  # for the default word combination in seq list, its the 12th shifted value
  print(i,"\t|\t",original,"\t|\t",nthRes)
  