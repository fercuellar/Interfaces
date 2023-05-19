from concurrent import futures
import logging

import grpc
import coords_pb2
import coords_pb2_grpc
import rospy
from geometry_msgs.msg import PointStamped


class Comm(coords_pb2_grpc.CoordsCommServicer):
    """
    Clase que implementa el servicio CoordsCommServicer de gRPC.
    """
    def __init__(self):
        """
        Inicializa la clase Comm.
        """
        print('initialized')
        
    def getCoords(self, request, context):
        """
        Método que maneja la solicitud de obtener coordenadas.

        Args:
            request: La solicitud recibida del cliente gRPC.
            context: El contexto de la solicitud.

        Returns:
            Las coordenadas obtenidas como un objeto PointStamped de coords_pb2.
        """
        print('Call received')
        coords = rospy.wait_for_message("/coordsx100", PointStamped)
        coordenadas = coords_pb2.PointStamped(
                seq=coords.header.seq,
                stamp=int(coords.header.stamp.to_sec()),
                frame_id=coords.header.frame_id,
                x=coords.point.x,
                y=coords.point.y,
                z=coords.point.z)
        print(coordenadas)
        return coordenadas


def serve():
    """
    Función que inicia el servidor gRPC y se pone en espera de solicitudes.
    """
    port = '50055'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    coords_pb2_grpc.add_CoordsCommServicer_to_server(Comm(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    rospy.init_node('gRPC_server')
    logging.basicConfig()
    serve()
