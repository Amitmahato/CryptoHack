#! /usr/bin/env python3

import telnetlib
import json
import base64
import codecs

HOST = "socket.cryptohack.org"
PORT = 13377

tn = telnetlib.Telnet(HOST, PORT)

def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)

class Decoder():
  def __init__(self):
    self.level = 0
    self.challenge = []
    self.solution = []
    self.rot13 = lambda s : codecs.getencoder("rot-13")(s)[0]
    
  def addChallenge(self, challenge):
    self.challenge.append(challenge)
    self.level += 1
  
  def getLatestChallenge(self) -> dict:
    return self.challenge[-1]

  # 1. utf8
  def utf8Decoder(self,encodedValue:list) -> str:
    decodedValue = ""
    for integer in encodedValue:
      decodedValue += chr(integer)
    return decodedValue

  # 2. hex
  def hexDecoder(self,encodedValue:str) -> str:
    return bytes.fromhex(encodedValue).decode("ASCII")
  
  # 3. bigint
  def bigIntDecoder(self,encodedValue:str) -> str:
    return self.hexDecoder(encodedValue[2:])

  # 4. base64
  def base64Decoder(self, encodedValue:str) -> str:
    return base64.b64decode(encodedValue).decode("ASCII")
  
  # 5. rot13
  def rot13Decoder(self,encodedValue:str) -> str:
    return self.rot13(encodedValue)

  def decode(self):
    # get the last challenge added
    lastChallenge = self.getLatestChallenge()

    # extracte type and encoded data
    encodingType = lastChallenge['type']
    encodedValue = lastChallenge["encoded"]
    decodedValue = ""

    # match the type and use corresponding decoder
    if encodingType == "utf-8":     # 1
      decodedValue = self.utf8Decoder(encodedValue)
    elif encodingType == "hex":     # 2
      decodedValue = self.hexDecoder(encodedValue)
    elif encodingType == "bigint":  # 3
      decodedValue = self.bigIntDecoder(encodedValue)
    elif encodingType == "base64":  # 4
      decodedValue = self.base64Decoder(encodedValue)
    elif encodingType == "rot13":    # 5
      decodedValue = self.rot13Decoder(encodedValue)
    else:
      print("Encoding Type Un-recognized : ",encodingType)
      return -1
    
    # append informations to solution
    self.solution.append({"level":self.level, "type":encodingType,"encoded":encodedValue,"decoded":decodedValue})
    return decodedValue
  
  # helper function to create json request
  def jsonValue(self,decodedValue:str) -> dict:
    return {"decoded":decodedValue}


def main():
  decoder = Decoder()

  # clear 100 levels to get flag in 101th request
  for i in range(101):
    received = json_recv()

    # if request is badly formated, we get error in response
    if type(received.get("error")).__name__ != 'NoneType':
      if received["error"] == "Invalid JSON":
        print("Wrong data sent at level : ", i+1)
        break
    
    # after 100 level, the flag is received
    if i+1 == 101:
      print("*** Congratulations ***")
      print("The flag is : ",received["flag"])
      f = open("./5. Encoding Challenge Solution.txt", "a")

      f.write("************************ Challenge Starts ************************\n\n")

      for solution in decoder.solution:
        f.write(json.dumps(solution))
        f.write("\n")

      toWriteFlag = "\n\nThe flag is : " + received["flag"]
      f.write(toWriteFlag)

      f.write("\n\n####################### Challenge Ends #######################\n\n\n\n\n")
      f.close()

      break
    
    # add new challenge to the decoder
    decoder.addChallenge(received)

    # run the decoder to get decoded value
    decoded = decoder.decode()
    
    # if decoding is successfull send the decoded value as json
    if(decoded != -1):
      print("Cleared level ",i+1,"\t",decoded)
      json_send(decoder.jsonValue(decoded))
    else:
      # if decoding fails at any point simply print out the solution till that point and stop
      print("Successfully solved : ",decoder.solution)
      break

if __name__ == "__main__":
  main()