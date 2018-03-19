from socket import *
from deal_with_client import deal_with_client
import os
port=12000
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
serverSocket.bind(("127.0.0.1",port))
serverSocket.listen(10)
print "The server is ready to be used"
while(1):
	connectionSocket,addr=serverSocket.accept()
	pid=os.fork()
	if(pid==0):
		serverSocket.close()
		deal_with_client(connectionSocket)
		os._exit(0)
	else:
		connectionSocket.close()
