import psutil as ps
import time
from src.utils.logger import setup_logger

logger = setup_logger(name='Monitoring System')


class MonitoringDisk:

    
    def format_bytes(self, value):
        """Format the value to GB with two decimal places."""
        return f"{value / (1024 ** 3):.2f} GB"
   
    def __disk_usage(self):
        return ps.disk_usage('/')

    def __swap_memory(self):
        return ps.swap_memory()    

    def _view_swap_memory(self):
        swap = self.__swap_memory()
        logger.info(f"Memória Swap Total: {self.format_bytes(swap.total)}")
        logger.info(f"Memória Swap Usada: {self.format_bytes(swap.used)}")
        logger.info(f"Memória Swap Livre: {self.format_bytes(swap.free)}")
        logger.info(f"Percentual de uso da Memória Swap: {swap.percent}%")

    def _view_metrics(self):
        disk_usage = self.__disk_usage()
        logger.info(f"Espaço total em disco: {self.format_bytes(disk_usage.total)}")
        logger.info(f"Espaço usado em disco: {self.format_bytes(disk_usage.used)}")
        logger.info(f"Espaço livre em disco: {self.format_bytes(disk_usage.free )}")
        logger.info(f"Percentual de uso do disco: {disk_usage.percent}%")

    def main(self):
        try:
            while True:
                self._view_metrics()
                self._view_swap_memory()
                time.sleep(1)
        except KeyboardInterrupt:
            logger.warning("Monitoramento de Disco finalizado")

control_disk = MonitoringDisk()
control_disk.main()            