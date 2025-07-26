// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('grpc');
var sentiric_media_v1_media_pb = require('../../../sentiric/media/v1/media_pb.js');

function serialize_sentiric_media_v1_AllocatePortRequest(arg) {
  if (!(arg instanceof sentiric_media_v1_media_pb.AllocatePortRequest)) {
    throw new Error('Expected argument of type sentiric.media.v1.AllocatePortRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_sentiric_media_v1_AllocatePortRequest(buffer_arg) {
  return sentiric_media_v1_media_pb.AllocatePortRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_sentiric_media_v1_AllocatePortResponse(arg) {
  if (!(arg instanceof sentiric_media_v1_media_pb.AllocatePortResponse)) {
    throw new Error('Expected argument of type sentiric.media.v1.AllocatePortResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_sentiric_media_v1_AllocatePortResponse(buffer_arg) {
  return sentiric_media_v1_media_pb.AllocatePortResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_sentiric_media_v1_ReleasePortRequest(arg) {
  if (!(arg instanceof sentiric_media_v1_media_pb.ReleasePortRequest)) {
    throw new Error('Expected argument of type sentiric.media.v1.ReleasePortRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_sentiric_media_v1_ReleasePortRequest(buffer_arg) {
  return sentiric_media_v1_media_pb.ReleasePortRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_sentiric_media_v1_ReleasePortResponse(arg) {
  if (!(arg instanceof sentiric_media_v1_media_pb.ReleasePortResponse)) {
    throw new Error('Expected argument of type sentiric.media.v1.ReleasePortResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_sentiric_media_v1_ReleasePortResponse(buffer_arg) {
  return sentiric_media_v1_media_pb.ReleasePortResponse.deserializeBinary(new Uint8Array(buffer_arg));
}


// MediaService, gerçek zamanlı medya (RTP) oturumlarını yönetir.
var MediaServiceService = exports.MediaServiceService = {
  // Yeni bir medya oturumu için boş bir RTP portu ayırır.
allocatePort: {
    path: '/sentiric.media.v1.MediaService/AllocatePort',
    requestStream: false,
    responseStream: false,
    requestType: sentiric_media_v1_media_pb.AllocatePortRequest,
    responseType: sentiric_media_v1_media_pb.AllocatePortResponse,
    requestSerialize: serialize_sentiric_media_v1_AllocatePortRequest,
    requestDeserialize: deserialize_sentiric_media_v1_AllocatePortRequest,
    responseSerialize: serialize_sentiric_media_v1_AllocatePortResponse,
    responseDeserialize: deserialize_sentiric_media_v1_AllocatePortResponse,
  },
  // Kullanılan bir RTP portunu serbest bırakır.
releasePort: {
    path: '/sentiric.media.v1.MediaService/ReleasePort',
    requestStream: false,
    responseStream: false,
    requestType: sentiric_media_v1_media_pb.ReleasePortRequest,
    responseType: sentiric_media_v1_media_pb.ReleasePortResponse,
    requestSerialize: serialize_sentiric_media_v1_ReleasePortRequest,
    requestDeserialize: deserialize_sentiric_media_v1_ReleasePortRequest,
    responseSerialize: serialize_sentiric_media_v1_ReleasePortResponse,
    responseDeserialize: deserialize_sentiric_media_v1_ReleasePortResponse,
  },
};

exports.MediaServiceClient = grpc.makeGenericClientConstructor(MediaServiceService, 'MediaService');
