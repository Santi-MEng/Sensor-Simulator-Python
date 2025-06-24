import random

#in this file we simulate the values for the sensors.
def read_temperature():
    #Generate values from 20 to 100 for temperature in centigrades
    return round(random.uniform(20.0,100.0),2)

def read_gas():
    #Generate values from 300 to 2000 ppm
    return round (random.uniform(300.0,2000.0),1)

def read_voltage():
    #Generate values from 3 to 12 volts
    return round(random.uniform(3.0,12.0),2)

if __name__ == "__main__":
    print("Temperature:", read_temperature(), "°C")
    print("Gas Level:", read_gas(), "ppm")
    print("Voltage:", read_voltage(), "V")