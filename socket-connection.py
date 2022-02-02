# Lets try an example to connect to the twitter server
import socket # We make use of the socket library so the first thing is to import the library.
import sys
 
 # Socket creation
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created.")
except socket.error as err:
    print ("socket creation failed with error %s" %(err))
 
# Specifying default port for socket
port = 80
 
# Get the host IP (resolve IP)
try:
    host_ip = socket.gethostbyname('www.twitter.com')
    print("twitter host IP: %s" %host_ip)
except socket.gaierror:
    print ("there was an error resolving the host")
    sys.exit()
 
# connecting to the server
s.connect((host_ip, port))
 
print ("The socket has successfully connected to twitter host ip above")