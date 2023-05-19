from concurrent import futures
import logging

import grpc
import coords_pb2
import coords_pb2_grpc
import rospy
from geometry_msgs.msg import PointStamped


class Comm(coords_pb2_grpc.CoordsCommServicer):
    def __init__(self):
        print('initialized')
    def getCoords(self, request, context):
        print('Call reveived')
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