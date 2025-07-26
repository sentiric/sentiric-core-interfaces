// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('grpc');
var sentiric_user_v1_user_pb = require('../../../sentiric/user/v1/user_pb.js');

function serialize_sentiric_user_v1_AuthenticateUserRequest(arg) {
  if (!(arg instanceof sentiric_user_v1_user_pb.AuthenticateUserRequest)) {
    throw new Error('Expected argument of type sentiric.user.v1.AuthenticateUserRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_sentiric_user_v1_AuthenticateUserRequest(buffer_arg) {
  return sentiric_user_v1_user_pb.AuthenticateUserRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_sentiric_user_v1_AuthenticateUserResponse(arg) {
  if (!(arg instanceof sentiric_user_v1_user_pb.AuthenticateUserResponse)) {
    throw new Error('Expected argument of type sentiric.user.v1.AuthenticateUserResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_sentiric_user_v1_AuthenticateUserResponse(buffer_arg) {
  return sentiric_user_v1_user_pb.AuthenticateUserResponse.deserializeBinary(new Uint8Array(buffer_arg));
}


// UserService, kullanıcı hesaplarını ve kimlik doğrulamasını yönetir.
var UserServiceService = exports.UserServiceService = {
  // Gelen bir çağrının kimliğini doğrular.
authenticateUser: {
    path: '/sentiric.user.v1.UserService/AuthenticateUser',
    requestStream: false,
    responseStream: false,
    requestType: sentiric_user_v1_user_pb.AuthenticateUserRequest,
    responseType: sentiric_user_v1_user_pb.AuthenticateUserResponse,
    requestSerialize: serialize_sentiric_user_v1_AuthenticateUserRequest,
    requestDeserialize: deserialize_sentiric_user_v1_AuthenticateUserRequest,
    responseSerialize: serialize_sentiric_user_v1_AuthenticateUserResponse,
    responseDeserialize: deserialize_sentiric_user_v1_AuthenticateUserResponse,
  },
};

exports.UserServiceClient = grpc.makeGenericClientConstructor(UserServiceService, 'UserService');
