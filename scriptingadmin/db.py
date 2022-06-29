import psutil


def store_db_value():
    """
        store the value get with psutil in the db
    """
    mem = psutil.virtual_memory()
    net = psutil.net_io_counters()
    bat = psutil.sensors_battery()
    temp = psutil.sensors_temperatures()


def get_value_interval(interval):
    """
        get values store in the db equivalent from the given interval
    Args:
        interval: a number representation of seconds before now

    Returns: all the rights values

    """
    values = []
    cpu = psutil.cpu_times_percent(interval)

    return values


def average_value(values):
    """
        get the average value from a given set of number value
    Args:
        values: list of value to sum up

    Returns: the average value

    """
    return 0
