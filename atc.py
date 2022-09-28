#Solicita - Data, Hora, Data e hora
import socket
def client(host = 'localhost', port=8082):
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_address = (host, port)
    print ("Conectando %s porta %s" % server_address)
    sock.connect(server_address)
    

    try:
        op = input("O que você deseja:\n1 - Data\n2 - Hora\n3 - Data e Hora\n0 - Sair\n")
        
        print ("Enviando %s" % op)
        
        sock.sendall(op.encode('utf-8'))
        op = sock.recv(2048)
        print(op)
    except socket.error as e:
        print ("Socket error: %s" %str(e))
    except Exception as e:
        print ("Other exception: %s" %str(e))
    finally:
        print ("Closing connection to the server")
        sock.close()

client()



