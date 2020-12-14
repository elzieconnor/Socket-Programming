# Connor Elzie
# Computer Science Department
# CSC 565: Computer Networks
# October 7, 2020
# Socket Programming Assignment 1
# TCP Client [python tcpclient.py]

#!/usr/bin/env python3

import socket
import pickle
import sys

# The port used by the server

PORT = 65432

# Continue to ask for user input so long as a value is enter
# Add user input into array and sent to server

while True:
    u_input = input("\nPlease enter command:\n").split()
    if len(u_input) == 0: # If no value is entered, exit the program
        break
    elif len(u_input) != 5: # If too many or too little values entered, return error
        print("You did not enter the command properly. Please try again.")
    elif int(u_input[2]) < 0 or int(u_input[3]) < 0 or float(u_input[4]) < 0: # If negative value entered, return error
        print("You cannot enter a negative value for integers. Please try again.")
    elif u_input[0] == 'cal' or u_input[0] == 'Cal': # Gather inputs into array
        a = u_input[0]
        b = u_input[1]
        c = int(u_input[2])
        d = int(u_input[3])
        e = float(u_input[4])
        arr = [a, b, c, d ,e]

        mes = pickle.dumps(arr) # Pickle array and send to server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((u_input[1], PORT))
            s.sendall(mes)
            data = s.recv(1024) # Receive array of answers from server and unpackage
            answer = pickle.loads(data)

        # Print answers provided by server based on user inputs

        print('\n$', u_input[2], 'loan')
        print('Monthly payment is $', f"{answer[0]:.2f}")
        print('Total payment is $', f"{answer[1]:.2f}")
