# Connor Elzie
# Computer Science Department
# CSC 565: Computer Networks
# October 7, 2020
# Socket Programming Assignment 1
# UDP Server [python udpclient.py]

#!/usr/bin/env python3

import socket
import pickle

HOST = '127.0.0.1'
PORT = 10000

# Create a UDP socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
# Retreive data package from client-side

sock.bind((HOST, PORT))
while True:
    data, address = sock.recvfrom(4096)
    if not data: # Break once complete data has been retrieved
        break

    # Unpackage data from client-side
    # Perform operations on data to determine monthly payment and total total_payment
    # Store answers into an array to be packaged and sent to client-side

    mes = pickle.loads(data)
    monthly_payment = (mes[2]*((mes[4]/100)/12))/(1-(1/(1+((mes[4]/100)/12))**(mes[3]*12)))
    total_payment = monthly_payment*12
    ans_array = [monthly_payment, total_payment]
    message = pickle.dumps(ans_array)
    sent = sock.sendto(message, address)
