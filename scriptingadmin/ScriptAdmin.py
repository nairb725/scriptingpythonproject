import psutil


def metrics():
    print(psutil.cpu_percent())
    print(psutil.net_io_counters())
    print(psutil.sensors_battery(), "platform not supported")
    print('memory used:', psutil.virtual_memory()[2], '%')
