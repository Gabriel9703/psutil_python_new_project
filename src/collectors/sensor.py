import psutil

# Verifica se a função está disponível
if hasattr(psutil, 'sensors_temperatures'):
    temps = psutil.sensors_temperatures()
    if temps:
        for name, entries in temps.items():
            print(f"Sensor: {name}")
            for entry in entries:
                print(f"  {entry.label or 'Sem rótulo'}: {entry.current}°C")
    else:
        print("Nenhum sensor de temperatura encontrado.")
else:
    print("A função 'sensors_temperatures' não está disponível no seu sistema.")
