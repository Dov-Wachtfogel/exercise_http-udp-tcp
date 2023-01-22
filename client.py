from socket import *
import requests

req = requests.get('http://127.0.0.1:5000/port')
#print(req.headers)
#print(req.url)
port = int(req.headers['Port_Number'])
serverSocket = socket(AF_INET, SOCK_DGRAM)

msgFromClient = "Cyber Himmelfarb"
bytesToSend = str.encode(msgFromClient)
serverAddressPort = ("127.0.0.1", port)
bufferSize = 1024
# Create a UDP socket at client side
UDPClientSocket = socket(family=AF_INET, type=SOCK_DGRAM)

# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddressPort)
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = msgFromServer[0].decode()
print(msg)
