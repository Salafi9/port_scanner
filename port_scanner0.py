#! /usr/bin/env python3
#-*-coding:utf8;-*-
__author__ = 'Ahmad Abdulnasir <ahmadabdulnasir9@gmail.com>'
__copyright__ = 'Copyright (c) 2017, salafi'
__version__ = "0.1t"

from threading import Thread
import socket
openPorts = []
closePorts = []
threads = []

def scan(host,port):
	s = socket.socket()
	result = s.connect_ex((host,port))
	print('*** Scanning port:  '+(str(port)))
	if result == 0:
		openPorts.append(port)
		print((str(port))+' -> open')
		s.close()
	else:
		closePorts.append(port)
		print((str(port))+' -> close')
		s.close()

def main():
	host = input('Host to scan: ')
	sPort = int(input('Starting scan port: '))
	ePort = int(input('Ending scan port: '))

	for i in range(sPort, ePort+1):
		t = Thread(target=scan, args=(host,i,))
		threads.append(t)
		t.start()
		[x.join() for x in threads]

	print("+++ Found {} open Ports".format(len(openPorts)))
	print("--- Found {} Closed Ports".format(len(closePorts)))

if __name__ == '__main__':
	main()
