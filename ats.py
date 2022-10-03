import socket
import threading
from datetime import datetime


def atender_requisicao(client):
    data = client.recv(2048).decode() #msg recebida do cliente
    match data:
        case "1":
            print('teste')
            date = str(datetime.today().strftime("%d/%m/%Y"))
            client.send(date.encode('utf-8'))
        case "2":
            date = str(datetime.now().strftime("%H:%M"))
            client.send(date.encode('utf-8'))
        case "3":
            date = str(datetime.now().strftime("%d/%m/%Y %H:%M"))
            client.send(date.encode('utf-8'))
    client.close()


def server(host = 'localhost', port=8082):

    sock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM) #criando socket
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #garante que o socket seja destruido

    server_address = (host, port)
    print ("Iniciando servidor na porta %s %s" % server_address)

    sock.bind(server_address) #associa o socket a uma porta
    sock.listen(5)
 
    while True:
        print ("Esperando solicitação do cliente")
        client, serv = sock.accept()

        t1 = threading.Thread(target = atender_requisicao,  args=(client,))
        t1.start()
server()