# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: sentiric/media/v1/media.proto
# Protobuf Python Version: 6.31.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    31,
    1,
    '',
    'sentiric/media/v1/media.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dsentiric/media/v1/media.proto\x12\x11sentiric.media.v1\"&\n\x13\x41llocatePortRequest\x12\x0f\n\x07\x63\x61ll_id\x18\x01 \x01(\t\"(\n\x14\x41llocatePortResponse\x12\x10\n\x08rtp_port\x18\x01 \x01(\r\"&\n\x12ReleasePortRequest\x12\x10\n\x08rtp_port\x18\x01 \x01(\r\"&\n\x13ReleasePortResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32\xcd\x01\n\x0cMediaService\x12_\n\x0c\x41llocatePort\x12&.sentiric.media.v1.AllocatePortRequest\x1a\'.sentiric.media.v1.AllocatePortResponse\x12\\\n\x0bReleasePort\x12%.sentiric.media.v1.ReleasePortRequest\x1a&.sentiric.media.v1.ReleasePortResponseBGZEgithub.com/sentiric/sentiric-core-interfaces/gen/go/sentiric/media/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentiric.media.v1.media_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZEgithub.com/sentiric/sentiric-core-interfaces/gen/go/sentiric/media/v1'
  _globals['_ALLOCATEPORTREQUEST']._serialized_start=52
  _globals['_ALLOCATEPORTREQUEST']._serialized_end=90
  _globals['_ALLOCATEPORTRESPONSE']._serialized_start=92
  _globals['_ALLOCATEPORTRESPONSE']._serialized_end=132
  _globals['_RELEASEPORTREQUEST']._serialized_start=134
  _globals['_RELEASEPORTREQUEST']._serialized_end=172
  _globals['_RELEASEPORTRESPONSE']._serialized_start=174
  _globals['_RELEASEPORTRESPONSE']._serialized_end=212
  _globals['_MEDIASERVICE']._serialized_start=215
  _globals['_MEDIASERVICE']._serialized_end=420
# @@protoc_insertion_point(module_scope)
