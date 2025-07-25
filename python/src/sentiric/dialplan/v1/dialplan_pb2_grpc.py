# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from sentiric.dialplan.v1 import dialplan_pb2 as sentiric_dot_dialplan_dot_v1_dot_dialplan__pb2

GRPC_GENERATED_VERSION = '1.74.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in sentiric/dialplan/v1/dialplan_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class DialplanServiceStub(object):
    """DialplanService, gelen çağrılar için yönlendirme kararları sağlar.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetDialplan = channel.unary_unary(
                '/sentiric.dialplan.v1.DialplanService/GetDialplan',
                request_serializer=sentiric_dot_dialplan_dot_v1_dot_dialplan__pb2.GetDialplanRequest.SerializeToString,
                response_deserializer=sentiric_dot_dialplan_dot_v1_dot_dialplan__pb2.GetDialplanResponse.FromString,
                _registered_method=True)


class DialplanServiceServicer(object):
    """DialplanService, gelen çağrılar için yönlendirme kararları sağlar.
    """

    def GetDialplan(self, request, context):
        """Belirtilen hedef için yönlendirme planını alır.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DialplanServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetDialplan': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDialplan,
                    request_deserializer=sentiric_dot_dialplan_dot_v1_dot_dialplan__pb2.GetDialplanRequest.FromString,
                    response_serializer=sentiric_dot_dialplan_dot_v1_dot_dialplan__pb2.GetDialplanResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sentiric.dialplan.v1.DialplanService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('sentiric.dialplan.v1.DialplanService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class DialplanService(object):
    """DialplanService, gelen çağrılar için yönlendirme kararları sağlar.
    """

    @staticmethod
    def GetDialplan(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/sentiric.dialplan.v1.DialplanService/GetDialplan',
            sentiric_dot_dialplan_dot_v1_dot_dialplan__pb2.GetDialplanRequest.SerializeToString,
            sentiric_dot_dialplan_dot_v1_dot_dialplan__pb2.GetDialplanResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
