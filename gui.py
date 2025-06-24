import tkinter as tk
from sensors import read_temperature, read_gas, read_voltage
from monitor import check_temperature, check_gas_level, check_voltage
from alerts import alert

TEMP_MAX = 70.0
GAS_MAX = 1000.0
VOLTAGE_RANGE = (4.5, 9.0)
after_id=None

def update_readings():
    temp = read_temperature()
    gas = read_gas()
    voltage = read_voltage()

    # Update labels
    temp_label.config(text=f"Temperature: {temp} °C", fg="red" if not check_temperature(temp) else "green")
    gas_label.config(text=f"Gas Level: {gas} ppm", fg="red" if not check_gas_level(gas) else "green")
    volt_label.config(text=f"Voltage: {voltage} V", fg="red" if not check_voltage(voltage) else "green")

    # Trigger alerts if needed
    if not check_temperature(temp):
        alert(f"Temperature too high: {temp}°C (max {TEMP_MAX}°C)")
    if not check_gas_level(gas):
        alert(f"Gas level too high: {gas} ppm (max {GAS_MAX} ppm)")
    if not check_voltage(voltage):
        alert(f"Voltage out of range: {voltage} V (expected between {VOLTAGE_RANGE[0]} and {VOLTAGE_RANGE[1]} V)")

    global after_id
    after_id = root.after(2000, update_readings)

def stop_updates():
    global after_id
    if after_id is not None:
        root.after_cancel(after_id)
        after_id = None
        print(" Monitoring stopped.")

# Setup GUI
root = tk.Tk()
root.title("Sensor Monitor")
#Temperature label
temp_label = tk.Label(root, font=("Arial", 14))
temp_label.pack(pady=5)
#Gas level label
gas_label = tk.Label(root, font=("Arial", 14))
gas_label.pack(pady=5)
#Voltage label
volt_label = tk.Label(root, font=("Arial", 14))
volt_label.pack(pady=5)
#Stop button
stop_button = tk.Button(root, text="Stop Monitoring", command=stop_updates, font=("Arial", 12), bg="red", fg="white")
stop_button.pack(pady=10)

update_readings()

root.mainloop()