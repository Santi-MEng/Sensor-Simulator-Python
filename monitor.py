from sensors import *
from alerts import alert
# in this file we set the thresholds for our system
TEMP_MAX= 70.0
GAS_MAX=1000.0
VOLT_RANGE=(4.5,9.0)

def check_temperature(temp):
    #it will catch the temp and make and assertion if the temperature is less equal than temp max
    return temp <= TEMP_MAX

def check_gas_level(gas):
    #It will catch the gas value and compare it with the Gas max level value
    return gas <= GAS_MAX

def check_voltage(voltage):
    #it will make a comparison of voltage between max and min voltage values
    return VOLT_RANGE[0] <= voltage <= VOLT_RANGE[1]

def run_monitor():
    temp = read_temperature()
    gas = read_gas()
    voltage = read_voltage()

    print("Monitoring...")
    if check_temperature(temp):
        print(f"Temperature: {temp} °C - OK")
    else:
        alert(f"Temperature too high: {temp}°C (max allowed is {TEMP_MAX}°C)")

    if check_gas_level(gas):
        print(f"Gas Level: {gas} ppm - OK")
    else:
        alert(f"Gas level too high: {gas} ppm (max allowed is {GAS_MAX} ppm)")

    if check_voltage(voltage):
        print(f"Voltage: {voltage} V - OK")
    else:
        alert(f"Voltage out of range: {voltage} V (expected between {VOLT_RANGE[0]} and {VOLT_RANGE[1]} V)")

    print(f"Temperature: {temp} °C - {'OK' if check_temperature(temp) else 'ALERT!'}")
    print(f"Gas Level:   {gas} ppm - {'OK' if check_gas_level(gas) else 'ALERT!'}")
    print(f"Voltage:     {voltage} V - {'OK' if check_voltage(voltage) else 'ALERT!'}")

if __name__ == "__main__":
    run_monitor()