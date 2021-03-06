# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: audio.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import quran.endpoints.grpc.shared_pb2 as shared__pb2
import quran.endpoints.grpc.entity_pb2 as entity__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='audio.proto',
  package='quran',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0b\x61udio.proto\x12\x05quran\x1a\x0cshared.proto\x1a\x0c\x65ntity.proto\"Y\n\x13\x41udioSingleResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0e\n\x06status\x18\x02 \x01(\t\x12$\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x16.quran.AudioSingleData\"W\n\x12\x41udioMultiResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0e\n\x06status\x18\x02 \x01(\t\x12#\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x15.quran.AudioMultiData\"O\n\x0f\x41udioSingleData\x12!\n\x05\x61udio\x18\x01 \x01(\x0b\x32\x12.quran.AudioEntity\x12\x19\n\x11number_of_results\x18\x02 \x01(\x05\"^\n\x0e\x41udioMultiData\x12!\n\x05\x61udio\x18\x01 \x03(\x0b\x32\x12.quran.AudioEntity\x12\x19\n\x11number_of_results\x18\x02 \x01(\x05\x12\x0e\n\x06\x63ursor\x18\x03 \x01(\t2\xa7\x03\n\x05\x41udio\x12?\n\x0b\x43reateAudio\x12\x12.quran.AudioEntity\x1a\x1a.quran.AudioSingleResponse\"\x00\x12?\n\rFindAudioById\x12\x10.quran.IDRequest\x1a\x1a.quran.AudioSingleResponse\"\x00\x12\x42\n\x11\x46indAudioByAyahId\x12\x10.quran.IDRequest\x1a\x19.quran.AudioMultiResponse\"\x00\x12\x45\n\x14\x46indAudioByEditionId\x12\x10.quran.IDRequest\x1a\x19.quran.AudioMultiResponse\"\x00\x12\x45\n\x0f\x46indArabicAudio\x12\x14.quran.FilterRequest\x1a\x1a.quran.AudioSingleResponse\"\x00\x12J\n\x14\x46indTranslationAudio\x12\x14.quran.FilterRequest\x1a\x1a.quran.AudioSingleResponse\"\x00\x62\x06proto3')
  ,
  dependencies=[shared__pb2.DESCRIPTOR,entity__pb2.DESCRIPTOR,])




_AUDIOSINGLERESPONSE = _descriptor.Descriptor(
  name='AudioSingleResponse',
  full_name='quran.AudioSingleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='quran.AudioSingleResponse.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='quran.AudioSingleResponse.status', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='quran.AudioSingleResponse.data', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=50,
  serialized_end=139,
)


_AUDIOMULTIRESPONSE = _descriptor.Descriptor(
  name='AudioMultiResponse',
  full_name='quran.AudioMultiResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='quran.AudioMultiResponse.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='quran.AudioMultiResponse.status', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='quran.AudioMultiResponse.data', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=141,
  serialized_end=228,
)


_AUDIOSINGLEDATA = _descriptor.Descriptor(
  name='AudioSingleData',
  full_name='quran.AudioSingleData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='audio', full_name='quran.AudioSingleData.audio', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='number_of_results', full_name='quran.AudioSingleData.number_of_results', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=230,
  serialized_end=309,
)


_AUDIOMULTIDATA = _descriptor.Descriptor(
  name='AudioMultiData',
  full_name='quran.AudioMultiData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='audio', full_name='quran.AudioMultiData.audio', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='number_of_results', full_name='quran.AudioMultiData.number_of_results', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cursor', full_name='quran.AudioMultiData.cursor', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=311,
  serialized_end=405,
)

_AUDIOSINGLERESPONSE.fields_by_name['data'].message_type = _AUDIOSINGLEDATA
_AUDIOMULTIRESPONSE.fields_by_name['data'].message_type = _AUDIOMULTIDATA
_AUDIOSINGLEDATA.fields_by_name['audio'].message_type = entity__pb2._AUDIOENTITY
_AUDIOMULTIDATA.fields_by_name['audio'].message_type = entity__pb2._AUDIOENTITY
DESCRIPTOR.message_types_by_name['AudioSingleResponse'] = _AUDIOSINGLERESPONSE
DESCRIPTOR.message_types_by_name['AudioMultiResponse'] = _AUDIOMULTIRESPONSE
DESCRIPTOR.message_types_by_name['AudioSingleData'] = _AUDIOSINGLEDATA
DESCRIPTOR.message_types_by_name['AudioMultiData'] = _AUDIOMULTIDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AudioSingleResponse = _reflection.GeneratedProtocolMessageType('AudioSingleResponse', (_message.Message,), {
  'DESCRIPTOR' : _AUDIOSINGLERESPONSE,
  '__module__' : 'audio_pb2'
  # @@protoc_insertion_point(class_scope:quran.AudioSingleResponse)
  })
_sym_db.RegisterMessage(AudioSingleResponse)

AudioMultiResponse = _reflection.GeneratedProtocolMessageType('AudioMultiResponse', (_message.Message,), {
  'DESCRIPTOR' : _AUDIOMULTIRESPONSE,
  '__module__' : 'audio_pb2'
  # @@protoc_insertion_point(class_scope:quran.AudioMultiResponse)
  })
_sym_db.RegisterMessage(AudioMultiResponse)

AudioSingleData = _reflection.GeneratedProtocolMessageType('AudioSingleData', (_message.Message,), {
  'DESCRIPTOR' : _AUDIOSINGLEDATA,
  '__module__' : 'audio_pb2'
  # @@protoc_insertion_point(class_scope:quran.AudioSingleData)
  })
_sym_db.RegisterMessage(AudioSingleData)

AudioMultiData = _reflection.GeneratedProtocolMessageType('AudioMultiData', (_message.Message,), {
  'DESCRIPTOR' : _AUDIOMULTIDATA,
  '__module__' : 'audio_pb2'
  # @@protoc_insertion_point(class_scope:quran.AudioMultiData)
  })
_sym_db.RegisterMessage(AudioMultiData)



_AUDIO = _descriptor.ServiceDescriptor(
  name='Audio',
  full_name='quran.Audio',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=408,
  serialized_end=831,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateAudio',
    full_name='quran.Audio.CreateAudio',
    index=0,
    containing_service=None,
    input_type=entity__pb2._AUDIOENTITY,
    output_type=_AUDIOSINGLERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='FindAudioById',
    full_name='quran.Audio.FindAudioById',
    index=1,
    containing_service=None,
    input_type=shared__pb2._IDREQUEST,
    output_type=_AUDIOSINGLERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='FindAudioByAyahId',
    full_name='quran.Audio.FindAudioByAyahId',
    index=2,
    containing_service=None,
    input_type=shared__pb2._IDREQUEST,
    output_type=_AUDIOMULTIRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='FindAudioByEditionId',
    full_name='quran.Audio.FindAudioByEditionId',
    index=3,
    containing_service=None,
    input_type=shared__pb2._IDREQUEST,
    output_type=_AUDIOMULTIRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='FindArabicAudio',
    full_name='quran.Audio.FindArabicAudio',
    index=4,
    containing_service=None,
    input_type=shared__pb2._FILTERREQUEST,
    output_type=_AUDIOSINGLERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='FindTranslationAudio',
    full_name='quran.Audio.FindTranslationAudio',
    index=5,
    containing_service=None,
    input_type=shared__pb2._FILTERREQUEST,
    output_type=_AUDIOSINGLERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_AUDIO)

DESCRIPTOR.services_by_name['Audio'] = _AUDIO

# @@protoc_insertion_point(module_scope)
