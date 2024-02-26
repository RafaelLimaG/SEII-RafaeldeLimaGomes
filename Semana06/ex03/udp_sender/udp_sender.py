import socket
import time
import sys

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
buf = 1024
file_name = sys.argv[1]

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(file_name.encode(), (UDP_IP, UDP_PORT))
print("Sending %s ..." % file_name)

try:
    with open(file_name, "rb") as f:
        data = f.read(buf)
        while data:
            if sock.sendto(data, (UDP_IP, UDP_PORT)):
                data = f.read(buf)
                time.sleep(0.02)  # Dê um pouco de tempo para o receptor salvar os dados
except FileNotFoundError:
    print(f"Arquivo '{file_name}' não encontrado.")
except Exception as e:
    print(f"Erro: {e}")

sock.close()
