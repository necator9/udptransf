#serverUDP
import socket  

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = "localhost";
port = 5000;
 
s.bind((host, port))

while(1) :
        d = s.recvfrom(1024)
        reply = d[0]
        addr = d[1]     
        s.sendto(reply, addr )         
        print 'Client message:  ' + reply
          
   
    