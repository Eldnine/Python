import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('www.pythonlearn.com', 80))
#mysocket.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')
mysocket.send('GET /code/intro-short.txt HTTP/1.1\n') #some servers have been upgraded to use HTTP/1.1, 
  #see updates at https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.23
mysocket.send('Host: www.pythonlearn.com\n\n')

while True:
    data = mysocket.recv(512)
    if ( len(data) < 1 ) :
        break
    print data;

mysocket.close()
