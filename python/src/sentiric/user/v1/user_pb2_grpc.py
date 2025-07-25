# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from sentiric.user.v1 import user_pb2 as sentiric_dot_user_dot_v1_dot_user__pb2

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
        + f' but the generated code in sentiric/user/v1/user_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class UserServiceStub(object):
    """UserService, kullanıcı hesaplarını ve kimlik doğrulamasını yönetir.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AuthenticateUser = channel.unary_unary(
                '/sentiric.user.v1.UserService/AuthenticateUser',
                request_serializer=sentiric_dot_user_dot_v1_dot_user__pb2.AuthenticateUserRequest.SerializeToString,
                response_deserializer=sentiric_dot_user_dot_v1_dot_user__pb2.AuthenticateUserResponse.FromString,
                _registered_method=True)


class UserServiceServicer(object):
    """UserService, kullanıcı hesaplarını ve kimlik doğrulamasını yönetir.
    """

    def AuthenticateUser(self, request, context):
        """Gelen bir çağrının kimliğini doğrular.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AuthenticateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.AuthenticateUser,
                    request_deserializer=sentiric_dot_user_dot_v1_dot_user__pb2.AuthenticateUserRequest.FromString,
                    response_serializer=sentiric_dot_user_dot_v1_dot_user__pb2.AuthenticateUserResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sentiric.user.v1.UserService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('sentiric.user.v1.UserService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class UserService(object):
    """UserService, kullanıcı hesaplarını ve kimlik doğrulamasını yönetir.
    """

    @staticmethod
    def AuthenticateUser(request,
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
            '/sentiric.user.v1.UserService/AuthenticateUser',
            sentiric_dot_user_dot_v1_dot_user__pb2.AuthenticateUserRequest.SerializeToString,
            sentiric_dot_user_dot_v1_dot_user__pb2.AuthenticateUserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
