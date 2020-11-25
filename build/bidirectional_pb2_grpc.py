# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from build import bidirectional_pb2 as bidirectional__pb2


class BidirectionalStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetServerResponse = channel.stream_stream(
                '/bidirectional.Bidirectional/GetServerResponse',
                request_serializer=bidirectional__pb2.Message.SerializeToString,
                response_deserializer=bidirectional__pb2.Message.FromString,
                )


class BidirectionalServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetServerResponse(self, request_iterator, context):
        """A bidirectional streaming RPC.

        Accepts a stream of Message sent while e route is being traversed,
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BidirectionalServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetServerResponse': grpc.stream_stream_rpc_method_handler(
                    servicer.GetServerResponse,
                    request_deserializer=bidirectional__pb2.Message.FromString,
                    response_serializer=bidirectional__pb2.Message.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'bidirectional.Bidirectional', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Bidirectional(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetServerResponse(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/bidirectional.Bidirectional/GetServerResponse',
            bidirectional__pb2.Message.SerializeToString,
            bidirectional__pb2.Message.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
