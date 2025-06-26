import psutil as ps

import time
from src.utils.logger import setup_logger

logger = setup_logger(name='Monitoring System')

class MonitoringNetwork:
    def __init__(self):
        self.rede = ps.net_if_addrs()
        self.net_statist = ps.net_io_counters()

    def mapeamento_rede(self):
        for interface, endereco in self.rede.items():
            print(f'Interface : {interface}')
            for e in endereco:
                print(f'Endereço : {e.address}')
                print(f'Tipo : {e.family}')
                print(f'Máscara : {e.netmask}')
                print(f'Broadcast : {e.broadcast}')

    def network_packet_send(self):
        return self.net_statist.bytes_recv
        
        
         / (1024 * 1024)
        print(f'Dados recebidos : {recebido:.2f} MB')
        enviado = self.pacotes.bytes_sent / (1024 * 1024)
        print(f'Dados enviados : {enviado:.2f} MB')
        pacotes_recebidos = self.pacotes.packets_recv
        print(f'Pacotes recebidos : {pacotes_recebidos}')
        pacotes_enviados = self.pacotes.packets_sent
        print(f'Pacotes enviados : {pacotes_enviados}')
        erros_recebidos = self.pacotes.errin
        print(f'Erros recebidos : {erros_recebidos}')
        erros_enviados = self.pacotes.errout
        print(f'Erros enviados : {erros_enviados}')
        print("-" * 30)

    
try:
    while True:
        pacotes_rede()
        time.sleep(5)  
        mapeamento_rede()   

except KeyboardInterrupt:
    print('Saindo...')