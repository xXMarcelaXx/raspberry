import Adafruit_DHT  
import time  
class temperatura:
    def __init__(self): 
        super().__init__()
    def temperatura(): 
        while True:
            sensor = Adafruit_DHT.DHT11 #Cambia por DHT22 y si usas dicho sensor
            pin = 11 #Pin en la raspberry donde conectamos el sensor
            humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
            
            print ('Humedad: ' , humedad)
            print ('Temperatura: ' , temperatura)
            
            time.sleep(1) #Cada segundo se evalúa el sensor