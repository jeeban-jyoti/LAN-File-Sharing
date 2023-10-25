# Import socket module 
import socket
import pickle			 

# Create a socket object 
s = socket.socket()		 

# Define the port on which you want to connect 
port = 44444
ip = input('@ip : ')

# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 

def receiveFile(sock, name):
    name = name.split('/')
    print(name)
    with open(name.pop(), 'wb') as file:
        while True:
            data = sock.recv(1024)
            if not data:
                break
            file.write(data)

# receive data from the server and decoding to get the string.
while True:
    try:
        r = pickle.loads(s.recv(1024))
        print(r)
    except:
        print("ERROR -- enter a valid path")
    l = input('$')
    s.send(bytes(l,'utf-8'))

    if(l[:5] == 'fetch'):
        try:
            receiveFile(s, l[5:])
        except:
            print("error")
        break

    if(l == 'exit'):
        break

# close the connection 
s.close()	 
	
