#clientUDP

import socket  

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = "localhost";
port = 5000;
while(1) :

        msg = raw_input('Your message: ')       
        s.sendto(msg, (host, port))
        d = s.recvfrom(1024)
        reply = d[0]
        addr = d[1]
         
        print 'Server reply : ' + reply
     