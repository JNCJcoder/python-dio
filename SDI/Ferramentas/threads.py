from threading import Thread
import time

def carro(velocidade, piloto):
    trajeto = 0
    
    while trajeto <= 100:
        print('Piloto: {} Km: {} '.format(piloto, trajeto))
        trajeto += velocidade
        time.sleep(0.5)


t_carro1 = Thread(target=carro, args=[10, 'Bruno'])
t_carro2 = Thread(target=carro, args=[20, 'Python'])

t_carro1.start()
t_carro2.start()
