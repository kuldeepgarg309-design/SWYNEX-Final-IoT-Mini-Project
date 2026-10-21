
import csv
import random
import time
from datetime import datetime

OUTPUT_FILE = "simulated_sensor_data.csv"
NUMBER_OF_READINGS = 20

def generate_reading():
    temperature = round(random.uniform(22, 42), 1)
    humidity = round(random.uniform(30, 75), 1)
    voltage = round(random.uniform(175, 240), 1)

    alerts = []
    if temperature > 35:
        alerts.append("HIGH_TEMPERATURE")
    if voltage < 200:
        alerts.append("LOW_VOLTAGE")

    status = "ALERT" if alerts else "NORMAL"

    return {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "temperature_c": temperature,
        "humidity_percent": humidity,
        "voltage_v": voltage,
        "status": status,
        "alert_details": "; ".join(alerts) if alerts else "None"
    }

def main():
    fieldnames = [
        "timestamp",
        "temperature_c",
        "humidity_percent",
        "voltage_v",
        "status",
        "alert_details"
    ]

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for number in range(NUMBER_OF_READINGS):
            reading = generate_reading()
            writer.writerow(reading)
            print(reading)
            time.sleep(0.1)

    print(f"\nSaved {NUMBER_OF_READINGS} simulated readings to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
