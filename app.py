from flask import *
import random
import _thread
from socket import *

app = Flask(__name__)
catched_ports = [5000]
serverSocket = socket(AF_INET, SOCK_DGRAM)
bufferSize = 1024


def random_port(catches_ports: list):
    p = random.randint(49152, 65533)
    if not p in catches_ports:
        return p
    return random_port(catches_ports)


def udp_server_theard(port: int):
    # Assign IP address and port number to socket
    serverSocket.bind(('', port))
    while True:
        bytesAddressPair = serverSocket.recvfrom(bufferSize)
        message = bytesAddressPair[0].decode()
        address = bytesAddressPair[1]
        if message == 'Cyber Himmelfarb':
            serverSocket.sendto('Victory!'.encode(), address)
        serverSocket.sendto('No Entry'.encode(), address)


@app.route('/port')
def port():  # put application's code here
    resp = Response()
    port = random_port(catched_ports)
    resp.headers['Port_Number'] = port
    catched_ports.append(port)
    _thread.start_new_thread(udp_server_theard, (port,))
    return resp


if __name__ == '__main__':
    app.run()
