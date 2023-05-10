import socket
from datetime import datetime
import os
meuIp = '10.15.2.98'
PORT = 12365
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((meuIp, PORT))
def comando( X ):
    if X == 'True':
        print("Tela Bloqueada !")
    if X == 'False':
        print("Tela Desbloqueada !")

while True:
    data, address = server_socket.recvfrom(1024)
    data_e_hora_atuais = datetime.now()
    print(f"SERVER | {address} | {data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')} | -> {data.decode()} ")
    comando(data.decode())