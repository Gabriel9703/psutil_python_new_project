import psutil as ps
import time
from src.utils.logger import setup_logger


logger = setup_logger(name = 'Monitoring System')


class MonitoringRam:
    def __mem_virt_total(self):
        return ps.virtual_memory().total / (1024**3)

    def __available_mem(self):
        return ps.virtual_memory().available / (1024**3)

    def __used_mem(self):
        return ps.virtual_memory().used / (1024**3)

    def __percent_mem_used(self):
        return ps.virtual_memory().percent

    def _view_metrics(self):
        logger.info(f"Memoria Total: {self.__mem_virt_total():.2f} GB")
        logger.info(f'Memoria Disponivel: {self.__available_mem():.2f} GB')
        logger.info(f'Memoria Usada: {self.__used_mem():.2f} GB')
        logger.info(f'Percentual de memoria em uso {self.__percent_mem_used()}%')
        
    def main(self):
        try:
            while True:
                self._view_metrics()
                time.sleep(1)
        except KeyboardInterrupt:
            logger.warning("Controle Finalizado")        

control_memory_ram = MonitoringRam()
control_memory_ram.main()




