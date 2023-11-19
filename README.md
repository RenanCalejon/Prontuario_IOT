# Prontuario_IOT
O prontuário médico online da Atlas-Med facilita a realização de consultas virtuais, possibilitando que pacientes obtenham orientações médicas sem a necessidade de deslocamento.


# Descrição Detalhada da Solução 🔍
Fizemos um dispositivo utilizando o Arduino ,PIR e LED RGB para proporciona uma solução interativa e visual para incentivar a atividade física, integrando-se ao prontuário  online da Atlas-Med para fornecer informações úteis sobre o estilo de vida dos pacientes.

### Funcionamento

•Coleta de Dados: o sensor de movimento detecta atividades físicas no ambiente.

•Processamento: o Arduino processa os dados para determinar a intensidade da atividade.

•Feedback Visual: o LED RGB emite diferentes cores de luz com base na intensidade da atividade física detectada.

•Registro no Prontuário: os dados sobre a atividade física e o feedback visual são registrados automaticamente no prontuário online da Atlas 

# Esquemas eletrônicos 

1.	Sensor de Movimento (sensor PIR )
2.	LED RGB
3.	Arduino Uno
4.	Placa de ensaio

# Instruções para replicar e testar a solução

1.	Acesso ao Tinkercad:

2.	Criar um Novo Projeto:

### 3.	Seleção dos Componentes:
   
• Arduino Uno

• Sensor PIR

•L ED RGB 

### 5.	Conexão dos Componentes:
•	Conecte a saída do sensor PIR ao pino digital 2 do Arduino.

•	Conecte o pino de catodo do LED RGB a um resistor de 220 ohms e, em seguida, ao terra do Arduino.

•	Conecte os pinos de ánodo dos LEDs RGB aos pinos digitais 9, 10 e 11 do Arduino.

•	Conecte o pino de cada LED RGB ao terra com resistores de 220 ohms.

•	Conecte o pino 5v do Arduino na entrada de potência do PIR

6.  Programação do Arduino:
•	Escreva o código necessário 

# Códigos-fonte ⬇️

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





