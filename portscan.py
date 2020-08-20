#!/bin/python3

import sys 
import socket
from datetime import datetime

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
else:
	print("syntax error")
	sys.exit()

print("-" * 50)
print("scanning target "+target)
print("time started: "+str(datetime.now()))
print("-" * 50)

try: 
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(10)
		result = s.connect_ex((target,port))
		print("checking{}".format(port))
		if result == 0:
			print("port {} is open".format(port))

except KeyboardInterrpt:
	print("\nExiting")

except socket.gaierror:
	print("hostname could not be resolved")
	sys.exit()
except socket.error:
	print("couldn't connect")
	sys.exit()

