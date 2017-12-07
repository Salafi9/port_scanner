#! /usr/bin/env python3
#-*-coding:utf8;-*-
__author__ = 'Ahmad Abdulnasir <ahmadabdulnasir9@gmail.com>'
__copyright__ = 'Copyright (c) 2017, salafi'
__version__ = "0.1t"

import socket
import sys, os
from datetime import datetime

os.system("clear")
rServer    = input("Host to scan: ")
print("*** Resolving Hostname .... ")
rServerIP  = socket.gethostbyname(rServer)

print("+" * 60)
print("Please wait, scanning remote host", rServerIP)
print("*" * 60)

sTime = datetime.now()

try:
    for port in range(1,1001):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((rServerIP, port))
        if result == 0:
            print("Port {}: is Open".format(port))
        sock.close()
except KeyboardInterrupt:
    print(" ---  Keyboard Interupt with Ctrl+C\n\t Exiting ....")
    sys.exit(0)
except socket.gaierror:
    print('---  Hostname could not be resolved.\n\t Exiting ....')
    sys.exit(1)
except socket.error:
    print("--- Couldn't connect to server\n\t Check Your Internet Connection")
    sys.exit(1)
eTime = datetime.now()

lTime =  eTime - sTime
print(' +++ Scanning Completed in: ', lTime)
