# Connor Elzie
# ce19877@live.missouristate.edu
# Computer Science Department
# CSC 565: Computer Networks
# October 7, 2020
# Socket Programming Assignment 1

# These programs are designed to emulate a client-server connection where 
# information is sent and retrieved between the two of them. The client-side 
# retrieves commands from the user and sends them to the server side. The server 
# then performs the necessary calculations before sending them back to the client 
# in the form of an array to be unpackaged and printed.

# TCPClient.py
# Client side that uses TCP

# TCPServer.py
# Server side that uses TCP

# UDPClient.py
# Client side that uses UDP

# UDPServer.py
# Server side that uses UDP

# RUNNING THE PROGRAMS
# In order to run the programs, you must first open the command line in the
# master folder and open the server via the follow command.

# python tcpserver.py / python udpserver.py

# Then, open the corresponding client with the following command via a
# different command terminal.

# python tcpclient.py / python udpclient.py

# You will be prompted to enter a command. The format should be as follows.

# "Cal" [HOST] [LOAN AMMOUNT] [MONTHS] [INTEREST RATE]

# The programs use Python Pickle in order to package an array of inputs to send 
# back and forth between client and server.

# CURRENT BUGS
#