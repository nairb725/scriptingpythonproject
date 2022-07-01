import psutil
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate an API token from the "API Tokens Tab" in the UI
token = "pVgJdDDf3MQGikSdaoBfjCovDRR_TcPoUxNW11vmzftXtG3WV5sx5o473gpXam8mDroFqE888dUs0wHDl-qOBQ=="
org = "b6548341542107d5"
bucket = "scripting"


def metrics():
    """
      link to influx bdd/create database/get computer information§right it down on the bdd and stop the program
    """

    with InfluxDBClient(url="http://localhost:8086", token=token, org=org) as client:
        write_api = client.write_api(write_options=SYNCHRONOUS)
        data = {
            "measurement": "measure",
            "fields": {
                "cpu_percent": psutil.cpu_percent(),
                'net': psutil.net_io_counters().packets_sent,
                'power': psutil.sensors_battery().percent,
                "ram": psutil.virtual_memory()[2]
            }
        }
        print(data)
        write_api.write(bucket, org, data)
