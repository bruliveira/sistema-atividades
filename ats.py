from datetime import date
from datetime import datetime

import socket

def server(host = 'localhost', port=8082):
    data_payload = 2048 
    
    sock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
    
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server_address = (host, port)
    print ("Iniciando servidor na porta %s %s" % server_address)
    sock.bind(server_address)
    
    sock.listen(1)
    i = 0

    atual = datetime.now()
    hora = atual.strftime('%H:%M:%S')
    hora_data = atual.strftime('%d/%m/%Y /%H:%M:%S')
    data = atual.strftime('%d/%m/%Y')


    while True:
        print ("Esperando mensagem do cliente")
        client, address = sock.accept()
        op = client.recv(data_payload)
        '''
        o que fazer com a mensagem recebida ?
        '''
        if(op == 1):
            print("-"*10, "Data", "-"*10,)
            print("gfg",data)
        if(op == 2):
            print("-"*10, "Hora", "-"*10,)
            print(hora)
        if(op == 3):
            print("-"*10, "Data e Hora", "-"*10,)
            print(hora_data)
        if(op == 0):
            print("Tchauu")     






      
        





        

server()

