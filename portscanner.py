#!/usr/bin/python3
import socket
import sys
import threading
import time
usage="python3 PortScanner.py TARGET START_PORT END_PORT"

#sys.argv counts no. of arguments in cli

print("-"*70)
print("Python Simple Port Scanner")
print("-"*70)

start_time=time.time()

if (len(sys.argv) !=4):
    print(usage)
    sys.exit()
    
try:
    target=socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Name resolution error")
    sys.exit()
    
start_port=int(sys.argv[2])
end_port=int(sys.argv[3])

print("Scanning Target",target)

def scan_port(port):
    print("Scanning port:",port)
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #if connection fails connect_ex it returns error number and doesnt terminate program unlike connect
    s.settimeout(2)
    conn=s.connect_ex((target,port))
    if(not conn):
        print("Port {} is Open".format(port))
    s.close()
    
for port in range(start_port,end_port+1):
    thread=threading.Thread(target=scan_port,args=(port,))
    thread.start()

end_time=time.time()
print("Time elapsed:",end_time-start_time,'s')