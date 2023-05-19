from __future__ import print_function

import logging

import grpc
import midterm.Scripts.protos.coords_pb2 as coords_pb2
import midterm.Scripts.protos.coords_pb2_grpc as coords_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50053') as channel:
        stub = coords_pb2_grpc.CoordsCommStub(channel)
        response = stub.getCoords(coords_pb2.Empty())
        print("Coords received: " + str(response))


if __name__ == '__main__':
    logging.basicConfig()
    run()