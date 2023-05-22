from __future__ import print_function
import logging
import grpc
import serial
import coords_pb2 as coords_pb2
import coords_pb2_grpc as coords_pb2_grpc
import time


def send_to_arduino(data):
    """
    Función para enviar datos a Arduino a través de la conexión serial.

    Args:
        data: Los datos a enviar a Arduino.

    """
    # Configurar la conexión serial con Arduino
    port = '/dev/ttyACM1'  # Cambia esto al puerto serial correcto en tu sistema
    baudrate = 9600  # La velocidad de transmisión debe coincidir con la configuración en Arduino
    ser = serial.Serial(port, baudrate)

    # Enviar datos a Arduino
    ser.write(data.encode())

    # Cerrar la conexión serial
    ser.close()


def run():
    """
    Función que establece una conexión gRPC con el servidor y obtiene coordenadas.

    """
    with grpc.insecure_channel('localhost:50056') as channel:
        stub = coords_pb2_grpc.CoordsCommStub(channel)
        response = stub.getCoords(coords_pb2.Empty())
        print("Coords received: " + str(response))

        # Enviar la respuesta a Arduino
        send_to_arduino(str(response))
        
        # Agregar una pausa para dar tiempo a Arduino a enviar la respuesta
        time.sleep(1)  # Pausa de 1 segundo



if __name__ == '__main__':
    logging.basicConfig()
    run()
