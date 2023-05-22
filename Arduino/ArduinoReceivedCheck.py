import serial

def receive_from_arduino():
    """
    Función para recibir datos desde Arduino a través de la conexión serial.

    Returns:
        Los datos recibidos desde Arduino.

    """
    # Configurar la conexión serial con Arduino
    port = '/dev/ttyACM1'  # Cambia esto al puerto serial correcto en tu sistema
    baudrate = 9600  # La velocidad de transmisión debe coincidir con la configuración en Arduino
    ser = serial.Serial(port, baudrate)

    # Leer datos desde Arduino
    while True:
        if ser.in_waiting > 0:
            arduino_response = ser.readline().decode().strip()
            print("Arduino response: " + arduino_response)

    # Cerrar la conexión serial
    ser.close()


if __name__ == '__main__':
    # Leer y mostrar la respuesta de Arduino
    receive_from_arduino()
