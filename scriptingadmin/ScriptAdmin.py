import psutil

print(psutil.cpu_percent(interval=1))
print(psutil.net_io_counters())
# print(psutil.sensors_temperatures())
print('memory % used:', psutil.virtual_memory()[2])