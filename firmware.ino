#include <WiFiNINA.h>
#include <Arduino_LSM6DS3.h>
#include <ArduinoJson.h>

void setup() {
  Serial.begin(9600);
  if (!IMU.begin()) { while (1); }
  // WiFi connection logic for Nano 33 IoT
}

void loop() {
  float x, y, z;
  if (IMU.accelerationAvailable()) {
    IMU.readAcceleration(x, y, z);
    float totalG = sqrt(x*x + y*y + z*z);

    if (totalG > 3.0) { // Impact Threshold
      sendSOS(totalG);
    }
  }
  delay(100);
}

void sendSOS(float force) {
  WiFiClient client;
  // HTTP POST logic to send "force" to Python dashboard
  Serial.print("Impact Detected: ");
  Serial.println(force);
}
