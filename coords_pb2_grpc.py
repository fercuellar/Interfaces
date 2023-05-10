# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import coords_pb2 as coords__pb2


class CoordServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetCoords = channel.unary_stream(
                '/coords.CoordService/GetCoords',
                request_serializer=coords__pb2.CoordRequest.SerializeToString,
                response_deserializer=coords__pb2.CoordResponse.FromString,
                )


class CoordServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetCoords(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CoordServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetCoords': grpc.unary_stream_rpc_method_handler(
                    servicer.GetCoords,
                    request_deserializer=coords__pb2.CoordRequest.FromString,
                    response_serializer=coords__pb2.CoordResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'coords.CoordService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CoordService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetCoords(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/coords.CoordService/GetCoords',
            coords__pb2.CoordRequest.SerializeToString,
            coords__pb2.CoordResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)