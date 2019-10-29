# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: StrategyService.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Share import Type_pb2 as Share_dot_Type__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='StrategyService.proto',
  package='QuoteResearch.Service.StrategyService',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x15StrategyService.proto\x12%QuoteResearch.Service.StrategyService\x1a\x10Share/Type.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"0\n\x0cStrategyInfo\x12\x12\n\nStrategyID\x18\x01 \x01(\t\x12\x0c\n\x04Info\x18\x02 \x01(\t\",\n\x16GetStrategyInfoRequest\x12\x12\n\nStrategyID\x18\x01 \x01(\t\"d\n\x17GetStrategyInfoResponse\x12I\n\x0cStrategyInfo\x18\x01 \x01(\x0b\x32\x33.QuoteResearch.Service.StrategyService.StrategyInfo\"\xa8\x01\n\x17GetStrategyListResponse\x12\x0e\n\x06Result\x18\x01 \x01(\x05\x12\x32\n\x0eLastUpdateTime\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12I\n\x0cStrategyInfo\x18\x03 \x03(\x0b\x32\x33.QuoteResearch.Service.StrategyService.StrategyInfo\".\n\x1bGetQuoteStrategyPairRequest\x12\x0f\n\x07QuoteID\x18\x01 \x01(\t\"F\n\x1cGetQuoteStrategyPairResponse\x12\x0e\n\x06Result\x18\x01 \x01(\x05\x12\x16\n\x0eStrategyIDList\x18\x03 \x03(\t2\xca\x03\n\x0fStrategyService\x12\x90\x01\n\x0fGetStrategyInfo\x12=.QuoteResearch.Service.StrategyService.GetStrategyInfoRequest\x1a>.QuoteResearch.Service.StrategyService.GetStrategyInfoResponse\x12\x81\x01\n\x0fGetStrategyList\x12..QuoteResearch.Service.Share.Type.EmptyRequest\x1a>.QuoteResearch.Service.StrategyService.GetStrategyListResponse\x12\x9f\x01\n\x14GetQuoteStrategyPair\x12\x42.QuoteResearch.Service.StrategyService.GetQuoteStrategyPairRequest\x1a\x43.QuoteResearch.Service.StrategyService.GetQuoteStrategyPairResponseb\x06proto3')
  ,
  dependencies=[Share_dot_Type__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_STRATEGYINFO = _descriptor.Descriptor(
  name='StrategyInfo',
  full_name='QuoteResearch.Service.StrategyService.StrategyInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='StrategyID', full_name='QuoteResearch.Service.StrategyService.StrategyInfo.StrategyID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Info', full_name='QuoteResearch.Service.StrategyService.StrategyInfo.Info', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=163,
)


_GETSTRATEGYINFOREQUEST = _descriptor.Descriptor(
  name='GetStrategyInfoRequest',
  full_name='QuoteResearch.Service.StrategyService.GetStrategyInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='StrategyID', full_name='QuoteResearch.Service.StrategyService.GetStrategyInfoRequest.StrategyID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=165,
  serialized_end=209,
)


_GETSTRATEGYINFORESPONSE = _descriptor.Descriptor(
  name='GetStrategyInfoResponse',
  full_name='QuoteResearch.Service.StrategyService.GetStrategyInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='StrategyInfo', full_name='QuoteResearch.Service.StrategyService.GetStrategyInfoResponse.StrategyInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=211,
  serialized_end=311,
)


_GETSTRATEGYLISTRESPONSE = _descriptor.Descriptor(
  name='GetStrategyListResponse',
  full_name='QuoteResearch.Service.StrategyService.GetStrategyListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Result', full_name='QuoteResearch.Service.StrategyService.GetStrategyListResponse.Result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='LastUpdateTime', full_name='QuoteResearch.Service.StrategyService.GetStrategyListResponse.LastUpdateTime', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='StrategyInfo', full_name='QuoteResearch.Service.StrategyService.GetStrategyListResponse.StrategyInfo', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=314,
  serialized_end=482,
)


_GETQUOTESTRATEGYPAIRREQUEST = _descriptor.Descriptor(
  name='GetQuoteStrategyPairRequest',
  full_name='QuoteResearch.Service.StrategyService.GetQuoteStrategyPairRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='QuoteID', full_name='QuoteResearch.Service.StrategyService.GetQuoteStrategyPairRequest.QuoteID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=484,
  serialized_end=530,
)


_GETQUOTESTRATEGYPAIRRESPONSE = _descriptor.Descriptor(
  name='GetQuoteStrategyPairResponse',
  full_name='QuoteResearch.Service.StrategyService.GetQuoteStrategyPairResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Result', full_name='QuoteResearch.Service.StrategyService.GetQuoteStrategyPairResponse.Result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='StrategyIDList', full_name='QuoteResearch.Service.StrategyService.GetQuoteStrategyPairResponse.StrategyIDList', index=1,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=532,
  serialized_end=602,
)

_GETSTRATEGYINFORESPONSE.fields_by_name['StrategyInfo'].message_type = _STRATEGYINFO
_GETSTRATEGYLISTRESPONSE.fields_by_name['LastUpdateTime'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETSTRATEGYLISTRESPONSE.fields_by_name['StrategyInfo'].message_type = _STRATEGYINFO
DESCRIPTOR.message_types_by_name['StrategyInfo'] = _STRATEGYINFO
DESCRIPTOR.message_types_by_name['GetStrategyInfoRequest'] = _GETSTRATEGYINFOREQUEST
DESCRIPTOR.message_types_by_name['GetStrategyInfoResponse'] = _GETSTRATEGYINFORESPONSE
DESCRIPTOR.message_types_by_name['GetStrategyListResponse'] = _GETSTRATEGYLISTRESPONSE
DESCRIPTOR.message_types_by_name['GetQuoteStrategyPairRequest'] = _GETQUOTESTRATEGYPAIRREQUEST
DESCRIPTOR.message_types_by_name['GetQuoteStrategyPairResponse'] = _GETQUOTESTRATEGYPAIRRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StrategyInfo = _reflection.GeneratedProtocolMessageType('StrategyInfo', (_message.Message,), {
  'DESCRIPTOR' : _STRATEGYINFO,
  '__module__' : 'StrategyService_pb2'
  # @@protoc_insertion_point(class_scope:QuoteResearch.Service.StrategyService.StrategyInfo)
  })
_sym_db.RegisterMessage(StrategyInfo)

GetStrategyInfoRequest = _reflection.GeneratedProtocolMessageType('GetStrategyInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSTRATEGYINFOREQUEST,
  '__module__' : 'StrategyService_pb2'
  # @@protoc_insertion_point(class_scope:QuoteResearch.Service.StrategyService.GetStrategyInfoRequest)
  })
_sym_db.RegisterMessage(GetStrategyInfoRequest)

GetStrategyInfoResponse = _reflection.GeneratedProtocolMessageType('GetStrategyInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSTRATEGYINFORESPONSE,
  '__module__' : 'StrategyService_pb2'
  # @@protoc_insertion_point(class_scope:QuoteResearch.Service.StrategyService.GetStrategyInfoResponse)
  })
_sym_db.RegisterMessage(GetStrategyInfoResponse)

GetStrategyListResponse = _reflection.GeneratedProtocolMessageType('GetStrategyListResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSTRATEGYLISTRESPONSE,
  '__module__' : 'StrategyService_pb2'
  # @@protoc_insertion_point(class_scope:QuoteResearch.Service.StrategyService.GetStrategyListResponse)
  })
_sym_db.RegisterMessage(GetStrategyListResponse)

GetQuoteStrategyPairRequest = _reflection.GeneratedProtocolMessageType('GetQuoteStrategyPairRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETQUOTESTRATEGYPAIRREQUEST,
  '__module__' : 'StrategyService_pb2'
  # @@protoc_insertion_point(class_scope:QuoteResearch.Service.StrategyService.GetQuoteStrategyPairRequest)
  })
_sym_db.RegisterMessage(GetQuoteStrategyPairRequest)

GetQuoteStrategyPairResponse = _reflection.GeneratedProtocolMessageType('GetQuoteStrategyPairResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETQUOTESTRATEGYPAIRRESPONSE,
  '__module__' : 'StrategyService_pb2'
  # @@protoc_insertion_point(class_scope:QuoteResearch.Service.StrategyService.GetQuoteStrategyPairResponse)
  })
_sym_db.RegisterMessage(GetQuoteStrategyPairResponse)



_STRATEGYSERVICE = _descriptor.ServiceDescriptor(
  name='StrategyService',
  full_name='QuoteResearch.Service.StrategyService.StrategyService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=605,
  serialized_end=1063,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetStrategyInfo',
    full_name='QuoteResearch.Service.StrategyService.StrategyService.GetStrategyInfo',
    index=0,
    containing_service=None,
    input_type=_GETSTRATEGYINFOREQUEST,
    output_type=_GETSTRATEGYINFORESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetStrategyList',
    full_name='QuoteResearch.Service.StrategyService.StrategyService.GetStrategyList',
    index=1,
    containing_service=None,
    input_type=Share_dot_Type__pb2._EMPTYREQUEST,
    output_type=_GETSTRATEGYLISTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetQuoteStrategyPair',
    full_name='QuoteResearch.Service.StrategyService.StrategyService.GetQuoteStrategyPair',
    index=2,
    containing_service=None,
    input_type=_GETQUOTESTRATEGYPAIRREQUEST,
    output_type=_GETQUOTESTRATEGYPAIRRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_STRATEGYSERVICE)

DESCRIPTOR.services_by_name['StrategyService'] = _STRATEGYSERVICE

# @@protoc_insertion_point(module_scope)
