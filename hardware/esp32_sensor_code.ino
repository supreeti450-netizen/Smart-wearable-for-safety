void setup() {
  Serial.begin(9600);
}

void loop() {
  int heartRate = random(70,130);
  float accel = random(0,40) / 10.0;

  Serial.print(heartRate);
  Serial.print(",");
  Serial.println(accel);

  delay(1000);
}
