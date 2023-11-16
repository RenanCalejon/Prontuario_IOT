#include <ArduinoIoTCloud.h>

const char THING_ID[] = "c0c490f0-b113-4933-bc23-bfe9f9864384";

const char THING_PSW[] = "MCSVU42F1AYFHYURU5GT";

CloudProperty<bool> movement;

int pirPin = 2;
int ledR = 9;
int ledG = 10;
int ledB = 11;

void setup() {
  ArduinoCloud.begin(ArduinoIoTPreferredConnection);

  pinMode(pirPin, INPUT);
  pinMode(ledR, OUTPUT);
  pinMode(ledG, OUTPUT);
  pinMode(ledB, OUTPUT);

  ArduinoCloud.begin(ArduinoIoTPreferredConnection);

  initProperties();

  delay(1500);
}

void loop() {
  ArduinoCloud.update();

  if (digitalRead(pirPin) == HIGH) {
    // Movimento detectado
    Serial.println("Movimento detectado");

    movement = true;

    analogWrite(ledR, 255);
    analogWrite(ledG, 0);
    analogWrite(ledB, 0);
    delay(1000);
  } else {
    Serial.println("Nenhum movimento detectado");

    movement = false;

    analogWrite(ledR, 0);
    analogWrite(ledG, 0);
    analogWrite(ledB, 255);
  }
}
void onMovementChange()  {
}
