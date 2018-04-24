import socket
import sys


HOST = "127.0.0.1"
PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print("[+] Conectado  com o servidor")

# pega o nome do arquivo para envio
f_send = "C:\\script.bat"
# abre o arquivo
with open(f_send, "rb") as f:
    # envia o arquivo
    print("[+] Enviando arquivo...")
    data = f.read()
    s.sendall(data)

    # fecha a conexão
    s.close()
    print("[-] Disconectado")
    sys.exit(0)