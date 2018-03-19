def parse(request):
	print request
	request=request.split()
	dict={}
	dict["method"]=request[0]
	b=request[1][1:]
	if(dict["method"]=="GET"):
		if '?' in b:
			b=b.split("=")
			if "+" in b[1]:
				b[1]=b[1][0:len(b[1])-1]
			if b[0]=="?song":
				b[1]=b[1]+".mp3"
			elif b[0]=="?video":
				b[1]=b[1]+".mp4"
			b=b[1]
			dict["file"]=b
			dict["query"]=True
		else:
			dict["file"]=b
			dict["query"]=False
	return dict
