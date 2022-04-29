pi@raspberrypi:/usr/local/lib $ cat prometheus_get.py 
#!/usr/bin/python
# -*- coding:utf-8 -*-

import ctypes
import prometheus_client
from prometheus_client import Gauge
from flask import Response, Flask

class SHTC3:
    def __init__(self):
        self.dll = ctypes.CDLL("/usr/local/lib/SHTC3.so")
        init = self.dll.init
        init.restype = ctypes.c_int
        init.argtypes = [ctypes.c_void_p]
        init(None)

    def SHTC3_Read_Temperature(self):
        temperature = self.dll.SHTC3_Read_TH
        temperature.restype = ctypes.c_float
        temperature.argtypes = [ctypes.c_void_p]
        return temperature(None)

    def SHTC3_Read_Humidity(self):
        humidity = self.dll.SHTC3_Read_RH
        humidity.restype = ctypes.c_float
        humidity.argtypes = [ctypes.c_void_p]
        return humidity(None)

app = Flask(__name__)
temperature = Gauge("Temperature", "temperature")
humidity = Gauge("Humidity", "humidity")

@app.route("/metrics1")
def t_value():
  #shtc3 = SHTC3()
  temperature.set(shtc3.SHTC3_Read_Temperature())
  #humidity.set(shtc3.SHTC3_Read_Humidity())
  return Response(prometheus_client.generate_latest(temperature),
          mimetype="text/plain")
          
@app.route("/metrics2")
def h_value():
  #shtc3 = SHTC3()
  #temperature.set(shtc3.SHTC3_Read_Temperature())
  humidity.set(shtc3.SHTC3_Read_Humidity())
  return Response(prometheus_client.generate_latest(humidity),
          mimetype="text/plain")
          
if __name__ == "__main__":
  shtc3 = SHTC3()
  app.run(host="0.0.0.0")

