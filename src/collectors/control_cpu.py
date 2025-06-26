import psutil as ps
import time

from src.utils.logger import setup_logger



logger = setup_logger(name='Monitoring System')



class MonitoringCpu:

    def __init__(self, threshold=80):
        self.threshold = threshold

    def __cpu_percent(self):
        return ps.cpu_percent(interval=1, percpu=False)
    
    def __all_cpu_percent(self):
        return ps.cpu_percent(interval=1, percpu=True)

    def count_cpu_cores_logical(self):
        return ps.cpu_count(logical=True)    

    def count_cpu_cores_physical(self):
        return ps.cpu_count(logical=False)

    def _view_metrics(self):
        cpu_usage = self.__cpu_percent()
        if cpu_usage > self.threshold:
            logger.warning(f"Alerta: Uso de CPU alto - {cpu_usage}%")
        else:
          logger.info(f"Uso de CPU: {cpu_usage}%")

    def _view_all_metrics(self):
        all_cpu_usage = self.__all_cpu_percent()
        for i, usage in enumerate(all_cpu_usage, start=1):
            if usage > self.threshold:
                logger.warning(f"Alerta: Uso de CPU do núcleo {i} alto - {usage}%")
            else:
                logger.info(f"Uso de CPU do núcleo {i}: {usage}%")

    def main(self):
        try:
            while True:
                self._view_metrics()
                self._view_all_metrics()
                time.sleep(1)
        except KeyboardInterrupt:
            logger.warning("Monitoramento de CPU finalizado")

control_cpu = MonitoringCpu()
print(f"Número de núcleos lógicos: {control_cpu.count_cpu_cores_logical()}")
print(f"Número de núcleos físicos: {control_cpu.count_cpu_cores_physical()}")

