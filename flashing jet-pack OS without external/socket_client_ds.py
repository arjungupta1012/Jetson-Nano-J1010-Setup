# import socket

# HOST = '127.0.0.1'
# PORT = 2005
# # create a socket and connect to the server
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((HOST, PORT))

# # loop to receive messages from the server
# while True:
#     message = s.recv(1024).decode()
#     print(message)


import socket
#import threading

HOST = '192.168.0.103'
PORT = 8000

# function to handle receiving messages from the server
def receive_thread(sock):
    while True:
        message = sock.recv(1024).decode()
        print(message)

# create a socket and connect to the server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((HOST, PORT))

# start a new thread to handle receiving messages
# # loop to send messages to the server (not needed in this case)
# while True:
#     threading.Thread(target=receive_thread, args=(s,)).start()
#     pass

while True:
    # Input = input('Hey there: ')
    # ClientMultiSocket.send(str.encode(Input))
    res = s.recvfrom(1024)
    print(res.decode())