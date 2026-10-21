
# SWYNEX Final IoT Mini-Project
## Simulated IoT Monitoring, Visualization and Alert Logic

### 1. Project Overview
This project demonstrates a remote IoT monitoring workflow using simulated sensor data, a web dashboard, threshold-based alerts, and a Python data-generation script.

The project is designed as an educational software simulation. No physical sensors or transformer are connected.

### 2. Objectives
- Generate timestamped sensor-like readings.
- Store sample readings in CSV format.
- Visualize simulated readings through a browser dashboard.
- Detect abnormal readings using simple threshold rules.
- Document the proposed IoT architecture and its limitations.

### 3. System Architecture
Conceptual data flow:

Sensor layer → ESP32 or similar controller → Wi-Fi/network → Data processing and storage → Web dashboard and alerts

In this project, sensor values are simulated in software. The physical sensor, controller, network transmission, and cloud-storage stages are conceptual only and have not been implemented or tested.

### 4. Project Files
- `index.html` — Interactive dashboard, simulated readings, alert logic, recent readings table, architecture overview, and limitations.
- `sensor_simulator.py` — Python script that generates timestamped sample readings and writes them to a CSV file.
- `simulated_sensor_data.csv` — Example dataset for demonstration.
- `README.md` — Project documentation.

### 5. Dashboard Features
- Simulated temperature, humidity, and voltage readings.
- Device status indicator.
- Recent readings table with timestamps.
- Buttons to test normal conditions, high temperature, low voltage, or both alerts.
- Responsive browser-based interface.

### 6. Alert Rules
The demonstration uses illustrative thresholds:
- High temperature: above 35 °C.
- Low voltage: below 200 V.

These thresholds are examples for software testing. They are not validated engineering limits or real transformer protection settings.

### 7. Python Simulator
Requirements: Python 3.8 or later. The script uses Python standard-library modules only.

Run the script from the project directory:

```bash
python sensor_simulator.py
```

The script generates 20 readings and writes them to `simulated_sensor_data.csv` in the current working directory. It overwrites that file when run.

The browser dashboard generates its own simulated readings; it does not currently read the CSV file or connect to the Python script.

### 8. How to Run the Dashboard
Open `index.html` in a modern web browser, or publish the repository using GitHub Pages.

Use the buttons under “Alert Logic Demonstration” to test the simulated alert conditions.

### 9. Limitations
- No physical sensors, transformer, ESP32, or other hardware is connected.
- No real-time network communication or cloud database is implemented.
- Dashboard values are generated in the browser and are separate from the Python-generated CSV dataset.
- Alert thresholds are illustrative and must not be used for real equipment protection.
- This project is a learning prototype, not a production monitoring or safety system.

### 10. Conclusion
This mini-project demonstrates the basic software concepts behind simulated IoT monitoring, data logging, browser-based visualization, and threshold-based alert logic.
