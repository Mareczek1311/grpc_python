# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nfs.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tnfs.proto\x12\x03nfs\"%\n\x07\x46ileReq\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04mode\x18\x02 \x01(\t\"\'\n\x07\x46ileRes\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\"6\n\x07ReadReq\x12\r\n\x05\x63hunk\x18\x01 \x01(\x05\x12\x0e\n\x06status\x18\x02 \x01(\x05\x12\x0c\n\x04name\x18\x03 \x01(\t\"\x17\n\x07ReadRes\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\"&\n\x08WriteReq\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x1a\n\x08WriteRes\x12\x0e\n\x06status\x18\x01 \x01(\x05\"8\n\x08LseekReq\x12\x0e\n\x06offset\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06whence\x18\x03 \x01(\x05\"\x1a\n\x08LseekRes\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x18\n\x08\x43loseReq\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1a\n\x08\x43loseRes\x12\x0e\n\x06status\x18\x01 \x01(\x05\x32\xf4\x01\n\x03NFS\x12$\n\x04Open\x12\x0c.nfs.FileReq\x1a\x0c.nfs.FileRes\"\x00\x12&\n\x06\x43reate\x12\x0c.nfs.FileReq\x1a\x0c.nfs.FileRes\"\x00\x12$\n\x04Read\x12\x0c.nfs.ReadReq\x1a\x0c.nfs.ReadRes\"\x00\x12\'\n\x05Write\x12\r.nfs.WriteReq\x1a\r.nfs.WriteRes\"\x00\x12\'\n\x05Lseek\x12\r.nfs.LseekReq\x1a\r.nfs.LseekRes\"\x00\x12\'\n\x05\x43lose\x12\r.nfs.CloseReq\x1a\r.nfs.CloseRes\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nfs_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_FILEREQ']._serialized_start=18
  _globals['_FILEREQ']._serialized_end=55
  _globals['_FILERES']._serialized_start=57
  _globals['_FILERES']._serialized_end=96
  _globals['_READREQ']._serialized_start=98
  _globals['_READREQ']._serialized_end=152
  _globals['_READRES']._serialized_start=154
  _globals['_READRES']._serialized_end=177
  _globals['_WRITEREQ']._serialized_start=179
  _globals['_WRITEREQ']._serialized_end=217
  _globals['_WRITERES']._serialized_start=219
  _globals['_WRITERES']._serialized_end=245
  _globals['_LSEEKREQ']._serialized_start=247
  _globals['_LSEEKREQ']._serialized_end=303
  _globals['_LSEEKRES']._serialized_start=305
  _globals['_LSEEKRES']._serialized_end=331
  _globals['_CLOSEREQ']._serialized_start=333
  _globals['_CLOSEREQ']._serialized_end=357
  _globals['_CLOSERES']._serialized_start=359
  _globals['_CLOSERES']._serialized_end=385
  _globals['_NFS']._serialized_start=388
  _globals['_NFS']._serialized_end=632
# @@protoc_insertion_point(module_scope)