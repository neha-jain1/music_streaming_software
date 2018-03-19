import time
def deal_with_client(connection):
	from parse import parse
	request=connection.recv(1024)
	request=parse(request)
	if(request["method"]=="GET" and request["file"]!="favicon.ico"):
		if(not request["query"]):
			b=open(request["file"],"rb")
			b=b.read()
		elif(request["query"]):
			if ".mp3" in request["file"]:
				b=open("play.html","rb")
			elif ".mp4" in request["file"]:
				b=open("play_video.html","rb")
			b=b.read()
			b=b%(request["file"],request["file"])
			f=open("f.html","w")
			f.write(b)
			f.close()
			b=open("f.html","rb")
			b=b.read()
		if ".html" in request["file"]:
			header = ("HTTP/1.1 200 OK\r\n"
        		    "Accept-Ranges: bytes\r\n"
        	  	    "Content-Length: 1000000000000000000000000000\r\n"
        		    "Keep-Alive: timeout=10, max=100\r\n"
        		    "Connection: Keep-Alive\r\n (or Connection: close)"
        		    "Content-Type: html/text\r\n"
        		    "\r\n")
		elif ".mp3" in request["file"]:
			header = ("HTTP/1.1 200 OK\r\n"
        		    "Accept-Ranges: bytes\r\n"
        	  	    "Content-Length: 1000000000000000000000000000\r\n"
        		    "Keep-Alive: timeout=10, max=100\r\n"
        		    "Connection: Keep-Alive\r\n (or Connection: close)"
        		    "Content-Type: audio/mpeg\r\n"
        		    "\r\n")
		elif ".mp4" in request["file"]:
			header = ("HTTP/1.1 200 OK\r\n"
        		    "Accept-Ranges: bytes\r\n"
        	  	    "Content-Length: 1000000000000000000000000000\r\n"
        		    "Keep-Alive: timeout=100000000, max=100\r\n"
        		    "Connection: Keep-Alive\r\n (or Connection: close)"
        		    "Content-Type: video/mp4\r\n"
        		    "\r\n")
		print request["file"]
		connection.send(header)
		if ".mp3" in request["file"]:
			for i in xrange(len(b)):
				connection.send(b[i])
		else:
			for i in xrange(len(b)):
				connection.send(b[i])
