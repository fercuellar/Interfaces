"""
@file
@brief Este es un ejemplo de aplicación Flask que utiliza gRPC para realizar llamadas a un servidor externo y mostrar los resultados en una plantilla HTML.
"""

from flask import Flask, render_template
import json
import grpc
import coords_pb2
import coords_pb2_grpc
from google.protobuf.json_format import MessageToJson

app = Flask(__name__, template_folder='templates')

def get_coords():
    """
    Realiza una llamada al servidor gRPC para obtener las coordenadas.
    
    @return La respuesta del servidor gRPC.
    """
    channel = grpc.insecure_channel('localhost:50052/coords')
    stub = coords_pb2_grpc.CoordsCommStub(channel)
    
    # Realizar la llamada al servidor gRPC
    response = stub.getCoords(coords_pb2.Empty())
    
    # Procesar la respuesta
    # ...
    return response

@app.route('/call-go-api')
def call_go_api():
    """
    Maneja la ruta '/call-go-api' de Flask y realiza la llamada al servidor gRPC.
    Los resultados se pasan a una plantilla HTML para su visualización.
    
    @return La plantilla HTML renderizada con los resultados.
    """
    coords = json.loads(MessageToJson(get_coords()))
    return render_template('home.html', coords=coords)

if __name__ == '__main__':
    app.run()
