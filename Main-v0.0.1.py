import pickle
import socket
import os

# Get the list of files and folders in the sharable directory
def fileList(extended_path = '', path = '/Users/jeeban_jyoti_patra/Desktop/Programs'):
    path = os.path.join(path, extended_path)
    return os.listdir(path)

# Update the app whenever a new version comes
def updateApp():
    pass

# Sending the requested file to the respective client
def sendFile(sock, path):
    print(path)
    with open(path, 'rb') as file:
        data = file.read(1024)
        while data:
            sock.send(data)
            data = file.read(1024)
    print("file sent..")

# Server connection -- always active -- Shows the file content
def serverConn():
    server = socket.socket()
    port = 44444

    server.bind(('', port))
    print ("socket binded to %s" %(port)) 

    server.listen(20)     
    print ("socket is listening")

    while True: 
        # Establish connection with client. 
        c, addr = server.accept()     
        print(c.getsockname())
        print ('Got connection from', addr )
        temp_extended_path = ''
        
        while 1:
            try:
                temp_data = pickle.dumps(fileList(temp_extended_path))

                c.send(temp_data)
                temp_extended_path = c.recv(1024).decode()

                print(temp_extended_path)

                if(temp_extended_path[:5] == 'fetch'):
                    temp_extended_path = temp_extended_path[6:]
                    sendFile(c, os.path.join( '/Users/jeeban_jyoti_patra/Desktop/Programs', temp_extended_path))
                    break

                if(temp_extended_path == 'exit'):
                    break
            except:
                print("error")
                break
        
        # Close the connection with the client 
        c.close()
	


if __name__ == '__main__':
    while 1:
        serverConn()