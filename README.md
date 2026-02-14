# ⛑️ Smart Industrial Safety Helmet

An advanced IoT wearable designed to protect workers in high-risk environments. It monitors physical impacts and orientation to detect accidents in real-time.

## 🚀 Features
- **Fall Detection:** Uses onboard IMU to detect sudden gravity changes (Free-fall) followed by an impact.
- **Impact Monitoring:** Tracks G-force intensity to identify head injuries even if the worker remains conscious.
- **Emergency SOS:** Automatically pings the dashboard with a "Man Down" alert.
- **Heat Stress Alerts:** Monitors ambient temperature inside the helmet to prevent heat exhaustion.

## ⚙️ Engineering Logic
- **Hardware:** Arduino Nano 33 IoT captures 6-axis motion data at 104Hz.
- **Software:** Python implements a threshold-based algorithm to distinguish between "putting the helmet down" and a "sudden human fall."
