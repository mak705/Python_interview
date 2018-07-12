##Import the socket, create the end point, connect the end point, sent the application, GET request down, recieve the data, close the socket 
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket is the library and socket is the method
mysock.connect(('www.py4inf.com', 80))

mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

while True:
 data = mysock.recv(512)
 if (len(data) < 1 ):
  break
 print data

mysock.close()
