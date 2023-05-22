// Definir la velocidad de comunicación serial
#define BAUD_RATE 9600

// Variable para almacenar los datos recibidos
String receivedData;

void setup() {
  // Inicializar la comunicación serial
  Serial.begin(BAUD_RATE);
  while (!Serial) {
    // Esperar a que se establezca la comunicación serial
  }
}

void loop() {
  if (Serial.available()) {
    // Leer los datos recibidos hasta que se alcance el final del mensaje
    char receivedChar = Serial.read();
    if (receivedChar != '\n') {
      receivedData += receivedChar;
    } else {
      // Concatenar el mensaje y la variable recibida
      String response = "Arduino recibió " + receivedData;
      
      // Enviar la respuesta a Python
      Serial.println(response);
      
      // Limpiar la variable para recibir nuevos datos
      receivedData = "";
    }
  }
}
