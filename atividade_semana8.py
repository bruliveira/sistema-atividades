'''
Escreva um programa em Python, que simule a fila de atendimento de um banco. O banco possui 3 caixas. O tempo de atendimento de cada cliente deve ser um tempo aleatório entre 3 a 10 segundos. Suponha que a fila tenha um tamanho fixo com 30 clientes em espera. Utilize um semáforo para fazer o gerenciamento dos recursos compartilhados (caixas) entre os clientes (threads). 
'''

import threading
import time
import random

semaforo = threading.Semaphore(3) #Define a quantidade de threading

def atendimento():
    semaforo.acquire()
    print(threading.currentThread().getName())
    time.sleep(random.randint(3,10))
    semaforo.release()

def lista_():
    return list(range(1,31))
    


if __name__=="__main__":
    t1 = threading.Thread(target=atendimento)
    t2 = threading.Thread(target=atendimento)
    t3 = threading.Thread(target=atendimento)
    
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

