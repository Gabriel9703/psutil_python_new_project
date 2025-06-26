import pytest
from unittest.mock import patch, MagicMock
import psutil
import time
from src.collectors.control_cpu import MonitoringCpu  # ajuste o import conforme sua estrutura

@pytest.fixture
def monitoring_cpu():
    return MonitoringCpu(threshold=80)

class TestMonitoringCpu:
    """Testes para a classe MonitoringCpu"""
    
    def test_initialization(self, monitoring_cpu):
        """Testa a inicialização da classe"""
        assert monitoring_cpu.threshold == 80
        
        custom_threshold = MonitoringCpu(threshold=90)
        assert custom_threshold.threshold == 90
    
    @patch('psutil.cpu_count')
    def test_count_cpu_cores_logical(self, mock_cpu_count, monitoring_cpu):
        """Testa a contagem de núcleos lógicos"""
        mock_cpu_count.return_value = 8
        assert monitoring_cpu.count_cpu_cores_logical() == 8
        mock_cpu_count.assert_called_once_with(logical=True)
    
    @patch('psutil.cpu_count')
    def test_count_cpu_cores_physical(self, mock_cpu_count, monitoring_cpu):
        """Testa a contagem de núcleos físicos"""
        mock_cpu_count.return_value = 4
        assert monitoring_cpu.count_cpu_cores_physical() == 4
        mock_cpu_count.assert_called_once_with(logical=False)
    
    @patch('psutil.cpu_percent')
    def test__cpu_percent(self, mock_cpu_percent, monitoring_cpu):
        """Testa o método privado __cpu_percent"""
        mock_cpu_percent.return_value = 50.0
        assert monitoring_cpu._MonitoringCpu__cpu_percent() == 50.0
        mock_cpu_percent.assert_called_once_with(interval=1, percpu=False)
    
    @patch('psutil.cpu_percent')
    def test__all_cpu_percent(self, mock_cpu_percent, monitoring_cpu):
        """Testa o método privado __all_cpu_percent"""
        mock_cpu_percent.return_value = [10.0, 20.0, 30.0, 40.0]
        assert monitoring_cpu._MonitoringCpu__all_cpu_percent() == [10.0, 20.0, 30.0, 40.0]
        mock_cpu_percent.assert_called_once_with(interval=1, percpu=True)
    
    @patch.object(MonitoringCpu, '_MonitoringCpu__cpu_percent')
    def test_view_metrics_below_threshold(self, mock_cpu_percent, monitoring_cpu, caplog):
        """Testa _view_metrics com uso abaixo do threshold"""
        mock_cpu_percent.return_value = 50.0
        monitoring_cpu._view_metrics()
        assert "Uso de CPU: 50.0%" in caplog.text
    
    @patch.object(MonitoringCpu, '_MonitoringCpu__cpu_percent')
    def test_view_metrics_above_threshold(self, mock_cpu_percent, monitoring_cpu, caplog):
        """Testa _view_metrics com uso acima do threshold"""
        mock_cpu_percent.return_value = 85.0
        monitoring_cpu._view_metrics()
        assert "Alerta: Uso de CPU alto - 85.0%" in caplog.text
    
    @patch.object(MonitoringCpu, '_MonitoringCpu__all_cpu_percent')
    def test_view_all_metrics(self, mock_all_cpu_percent, monitoring_cpu, caplog):
        """Testa _view_all_metrics com diferentes cenários"""
        # Simula 4 núcleos com usos variados
        mock_all_cpu_percent.return_value = [75.0, 85.0, 60.0, 90.0]
        monitoring_cpu._view_all_metrics()
        
        logs = caplog.text
        assert "Uso de CPU do núcleo 1: 75.0%" in logs
        assert "Alerta: Uso de CPU do núcleo 2 alto - 85.0%" in logs
        assert "Uso de CPU do núcleo 3: 60.0%" in logs
        assert "Alerta: Uso de CPU do núcleo 4 alto - 90.0%" in logs
    
    @patch.object(MonitoringCpu, '_view_metrics')
    @patch.object(MonitoringCpu, '_view_all_metrics')
    def test_main_loop(self, mock_view_all, mock_view_metrics, monitoring_cpu):
        """Testa o loop principal com KeyboardInterrupt"""
        # Simula o KeyboardInterrupt após 2 iterações
        mock_view_metrics.side_effect = [None, None, KeyboardInterrupt()]
        
        with patch('time.sleep') as mock_sleep:
            monitoring_cpu.main()
            
        assert mock_view_metrics.call_count == 2
        assert mock_view_all.call_count == 2
        mock_sleep.assert_called_with(1)