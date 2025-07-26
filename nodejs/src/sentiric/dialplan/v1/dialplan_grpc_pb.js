// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('grpc');
var sentiric_dialplan_v1_dialplan_pb = require('../../../sentiric/dialplan/v1/dialplan_pb.js');

function serialize_sentiric_dialplan_v1_GetDialplanRequest(arg) {
  if (!(arg instanceof sentiric_dialplan_v1_dialplan_pb.GetDialplanRequest)) {
    throw new Error('Expected argument of type sentiric.dialplan.v1.GetDialplanRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_sentiric_dialplan_v1_GetDialplanRequest(buffer_arg) {
  return sentiric_dialplan_v1_dialplan_pb.GetDialplanRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_sentiric_dialplan_v1_GetDialplanResponse(arg) {
  if (!(arg instanceof sentiric_dialplan_v1_dialplan_pb.GetDialplanResponse)) {
    throw new Error('Expected argument of type sentiric.dialplan.v1.GetDialplanResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_sentiric_dialplan_v1_GetDialplanResponse(buffer_arg) {
  return sentiric_dialplan_v1_dialplan_pb.GetDialplanResponse.deserializeBinary(new Uint8Array(buffer_arg));
}


// DialplanService, gelen çağrılar için yönlendirme kararları sağlar.
var DialplanServiceService = exports.DialplanServiceService = {
  // Belirtilen hedef için yönlendirme planını alır.
getDialplan: {
    path: '/sentiric.dialplan.v1.DialplanService/GetDialplan',
    requestStream: false,
    responseStream: false,
    requestType: sentiric_dialplan_v1_dialplan_pb.GetDialplanRequest,
    responseType: sentiric_dialplan_v1_dialplan_pb.GetDialplanResponse,
    requestSerialize: serialize_sentiric_dialplan_v1_GetDialplanRequest,
    requestDeserialize: deserialize_sentiric_dialplan_v1_GetDialplanRequest,
    responseSerialize: serialize_sentiric_dialplan_v1_GetDialplanResponse,
    responseDeserialize: deserialize_sentiric_dialplan_v1_GetDialplanResponse,
  },
};

exports.DialplanServiceClient = grpc.makeGenericClientConstructor(DialplanServiceService, 'DialplanService');
