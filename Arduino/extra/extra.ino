/**
 * @file
 * @brief Código de Arduino para la comunicación serial
 */

/**
 * @def BAUD_RATE
 * @brief Velocidad de comunicación serial
 */
#define BAUD_RATE 9600

/**
 * @var receivedData
 * @brief Variable para almacenar los datos recibidos
 */
String receivedData;

/**
 * @brief Configuración inicial del Arduino
 *
 * Inicializa la comunicación serial y espera hasta que se establezca la conexión.
 */
void setup() {
  // Inicializar la comunicación serial
  Serial.begin(BAUD_RATE);
  
  while (!Serial) {
    // Esperar a que se establezca la comunicación serial
  }
}

/**
 * @brief Función principal de Arduino
 *
 * Lee los datos recibidos por la comunicación serial y envía una respuesta a Python.
 */
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
