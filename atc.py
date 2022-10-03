#Solicita - Data, Hora, Data e hora
import socket

def client(host = 'localhost', port=8082):
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_address = (host, port) #destino
    print ("Conectando %s porta %s" % server_address)
    sock.connect(server_address)
    
    try:
        op = input("Consultar:\n1 - Data\n2 - Hora\n3 - Data e Hora\n")
        sock.send(op.encode('utf-8'))
        print(str(sock.recv(2048).decode()))
        print('\n')
    except socket.error as e:
        print ("Socket error: %s" %str(e))
    except Exception as e:
        print ("Other exception: %s" %str(e))
    finally:
        print ("Closing connection to the server")
        sock.close()
client()
