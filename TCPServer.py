# Connor Elzie
# Computer Science Department
# CSC 565: Computer Networks
# October 7, 2020
# Socket Programming Assignment 1
# TCP Server [python tcpservert.py]

#!/usr/bin/env python3

import socket
import pickle

HOST = '127.0.0.1'
PORT = 65432

# Bind and listen for client server response
# Retreive client-side input a packaged array

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
            data = conn.recv(1024) # Retrieve client-side package
            if not data: # If data fully retrieved
                break
            mes = pickle.loads(data) # Unpackage array for calculations

            # Loan payment calculator calculations
            # Append answers to array

            monthly_payment = (mes[2]*((mes[4]/100)/12))/(1-(1/(1+((mes[4]/100)/12))**(mes[3]*12)))
            total_payment = monthly_payment*12
            ans_array = [monthly_payment, total_payment]

            # Package array to send back to client-side

            message = pickle.dumps(ans_array)
            conn.sendall(message)
