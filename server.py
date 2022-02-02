# Import socket library
import socket			

# Create socket object, s
s = socket.socket()		
print ("Socket successfully created")

# reserve a port on your computer in computer to run from 
port = 12345			

# Next bind to the port
# Note that we have not typed any ip in the ip field, instead we have inputted an empty string
# This makes the server listen to requests coming from other computers on the network
s.bind(('', port))		
print ("socket binded to %s" %(port))

# Put the socket into listening mode
s.listen(5)	
print ("Socket is listening")		

# a forever loop until we interrupt it or
# an error occurs
while True:
    # Establish connection with client.
    c, addr = s.accept()
    print ('Got connection from', addr )

    # send a thank you message to the client. encoding to send byte type.
    c.send('Thank you for connecting'.encode())

    # Close the connection with the client
    c.close()

    # Breaking once connection closed
    break
