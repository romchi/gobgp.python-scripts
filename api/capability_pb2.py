# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: capability.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import gobgp_pb2 as gobgp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='capability.proto',
  package='gobgpapi',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10\x63\x61pability.proto\x12\x08gobgpapi\x1a\x0bgobgp.proto\";\n\x17MultiProtocolCapability\x12 \n\x06\x66\x61mily\x18\x01 \x01(\x0b\x32\x10.gobgpapi.Family\"\x18\n\x16RouteRefreshCapability\"\x1d\n\x1b\x43\x61rryingLabelInfoCapability\"q\n\x1e\x45xtendedNexthopCapabilityTuple\x12%\n\x0bnlri_family\x18\x01 \x01(\x0b\x32\x10.gobgpapi.Family\x12(\n\x0enexthop_family\x18\x02 \x01(\x0b\x32\x10.gobgpapi.Family\"U\n\x19\x45xtendedNexthopCapability\x12\x38\n\x06tuples\x18\x01 \x03(\x0b\x32(.gobgpapi.ExtendedNexthopCapabilityTuple\"Q\n\x1eGracefulRestartCapabilityTuple\x12 \n\x06\x66\x61mily\x18\x01 \x01(\x0b\x32\x10.gobgpapi.Family\x12\r\n\x05\x66lags\x18\x02 \x01(\r\"r\n\x19GracefulRestartCapability\x12\r\n\x05\x66lags\x18\x01 \x01(\r\x12\x0c\n\x04time\x18\x02 \x01(\r\x12\x38\n\x06tuples\x18\x03 \x03(\x0b\x32(.gobgpapi.GracefulRestartCapabilityTuple\")\n\x1b\x46ourOctetASNumberCapability\x12\n\n\x02\x61s\x18\x01 \x01(\r\"_\n\x16\x41\x64\x64PathCapabilityTuple\x12 \n\x06\x66\x61mily\x18\x01 \x01(\x0b\x32\x10.gobgpapi.Family\x12#\n\x04mode\x18\x02 \x01(\x0e\x32\x15.gobgpapi.AddPathMode\"E\n\x11\x41\x64\x64PathCapability\x12\x30\n\x06tuples\x18\x01 \x03(\x0b\x32 .gobgpapi.AddPathCapabilityTuple\" \n\x1e\x45nhancedRouteRefreshCapability\"h\n\'LongLivedGracefulRestartCapabilityTuple\x12 \n\x06\x66\x61mily\x18\x01 \x01(\x0b\x32\x10.gobgpapi.Family\x12\r\n\x05\x66lags\x18\x02 \x01(\r\x12\x0c\n\x04time\x18\x03 \x01(\r\"g\n\"LongLivedGracefulRestartCapability\x12\x41\n\x06tuples\x18\x01 \x03(\x0b\x32\x31.gobgpapi.LongLivedGracefulRestartCapabilityTuple\"\x1d\n\x1bRouteRefreshCiscoCapability\"h\n\x0e\x46QDNCapability\x12\x15\n\rhost_name_len\x18\x01 \x01(\r\x12\x11\n\thost_name\x18\x02 \x01(\t\x12\x17\n\x0f\x64omain_name_len\x18\x03 \x01(\r\x12\x13\n\x0b\x64omain_name\x18\x04 \x01(\t\"0\n\x11UnknownCapability\x12\x0c\n\x04\x63ode\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\x0c*L\n\x0b\x41\x64\x64PathMode\x12\r\n\tMODE_NONE\x10\x00\x12\x10\n\x0cMODE_RECEIVE\x10\x01\x12\r\n\tMODE_SEND\x10\x02\x12\r\n\tMODE_BOTH\x10\x03\x62\x06proto3'
  ,
  dependencies=[gobgp__pb2.DESCRIPTOR,])

_ADDPATHMODE = _descriptor.EnumDescriptor(
  name='AddPathMode',
  full_name='gobgpapi.AddPathMode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MODE_NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MODE_RECEIVE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MODE_SEND', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MODE_BOTH', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1205,
  serialized_end=1281,
)
_sym_db.RegisterEnumDescriptor(_ADDPATHMODE)

AddPathMode = enum_type_wrapper.EnumTypeWrapper(_ADDPATHMODE)
MODE_NONE = 0
MODE_RECEIVE = 1
MODE_SEND = 2
MODE_BOTH = 3



_MULTIPROTOCOLCAPABILITY = _descriptor.Descriptor(
  name='MultiProtocolCapability',
  full_name='gobgpapi.MultiProtocolCapability',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='family', full_name='gobgpapi.MultiProtocolCapability.family', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=43,
  serialized_end=102,
)


_ROUTEREFRESHCAPABILITY = _descriptor.Descriptor(
  name='RouteRefreshCapability',
  full_name='gobgpapi.RouteRefreshCapability',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=104,
  serialized_end=128,
)


_CARRYINGLABELINFOCAPABILITY = _descriptor.Descriptor(
  name='CarryingLabelInfoCapability',
  full_name='gobgpapi.CarryingLabelInfoCapability',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=130,
  serialized_end=159,
)


_EXTENDEDNEXTHOPCAPABILITYTUPLE = _descriptor.Descriptor(
  name='ExtendedNexthopCapabilityTuple',
  full_name='gobgpapi.ExtendedNexthopCapabilityTuple',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nlri_family', full_name='gobgpapi.ExtendedNexthopCapabilityTuple.nlri_family', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nexthop_family', full_name='gobgpapi.ExtendedNexthopCapabilityTuple.nexthop_family', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=161,
  serialized_end=274,
)


_EXTENDEDNEXTHOPCAPABILITY = _descriptor.Descriptor(
  name='ExtendedNexthopCapability',
  full_name='gobgpapi.ExtendedNexthopCapability',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tuples', full_name='gobgpapi.ExtendedNexthopCapability.tuples', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=276,
  serialized_end=361,
)


_GRACEFULRESTARTCAPABILITYTUPLE = _descriptor.Descriptor(
  name='GracefulRestartCapabilityTuple',
  full_name='gobgpapi.GracefulRestartCapabilityTuple',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='family', full_name='gobgpapi.GracefulRestartCapabilityTuple.family', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='flags', full_name='gobgpapi.GracefulRestartCapabilityTuple.flags', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=363,
  serialized_end=444,
)


_GRACEFULRESTARTCAPABILITY = _descriptor.Descriptor(
  name='GracefulRestartCapability',
  full_name='gobgpapi.GracefulRestartCapability',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='flags', full_name='gobgpapi.GracefulRestartCapability.flags', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time', full_name='gobgpapi.GracefulRestartCapability.time', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tuples', full_name='gobgpapi.GracefulRestartCapability.tuples', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=446,
  serialized_end=560,
)


_FOUROCTETASNUMBERCAPABILITY = _descriptor.Descriptor(
  name='FourOctetASNumberCapability',
  full_name='gobgpapi.FourOctetASNumberCapability',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='as', full_name='gobgpapi.FourOctetASNumberCapability.as', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=562,
  serialized_end=603,
)


_ADDPATHCAPABILITYTUPLE = _descriptor.Descriptor(
  name='AddPathCapabilityTuple',
  full_name='gobgpapi.AddPathCapabilityTuple',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='family', full_name='gobgpapi.AddPathCapabilityTuple.family', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mode', full_name='gobgpapi.AddPathCapabilityTuple.mode', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=605,
  serialized_end=700,
)


_ADDPATHCAPABILITY = _descriptor.Descriptor(
  name='AddPathCapability',
  full_name='gobgpapi.AddPathCapability',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tuples', full_name='gobgpapi.AddPathCapability.tuples', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=702,
  serialized_end=771,
)


_ENHANCEDROUTEREFRESHCAPABILITY = _descriptor.Descriptor(
  name='EnhancedRouteRefreshCapability',
  full_name='gobgpapi.EnhancedRouteRefreshCapability',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=773,
  serialized_end=805,
)


_LONGLIVEDGRACEFULRESTARTCAPABILITYTUPLE = _descriptor.Descriptor(
  name='LongLivedGracefulRestartCapabilityTuple',
  full_name='gobgpapi.LongLivedGracefulRestartCapabilityTuple',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='family', full_name='gobgpapi.LongLivedGracefulRestartCapabilityTuple.family', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='flags', full_name='gobgpapi.LongLivedGracefulRestartCapabilityTuple.flags', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time', full_name='gobgpapi.LongLivedGracefulRestartCapabilityTuple.time', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=807,
  serialized_end=911,
)


_LONGLIVEDGRACEFULRESTARTCAPABILITY = _descriptor.Descriptor(
  name='LongLivedGracefulRestartCapability',
  full_name='gobgpapi.LongLivedGracefulRestartCapability',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tuples', full_name='gobgpapi.LongLivedGracefulRestartCapability.tuples', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=913,
  serialized_end=1016,
)


_ROUTEREFRESHCISCOCAPABILITY = _descriptor.Descriptor(
  name='RouteRefreshCiscoCapability',
  full_name='gobgpapi.RouteRefreshCiscoCapability',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=1018,
  serialized_end=1047,
)


_FQDNCAPABILITY = _descriptor.Descriptor(
  name='FQDNCapability',
  full_name='gobgpapi.FQDNCapability',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='host_name_len', full_name='gobgpapi.FQDNCapability.host_name_len', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='host_name', full_name='gobgpapi.FQDNCapability.host_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain_name_len', full_name='gobgpapi.FQDNCapability.domain_name_len', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain_name', full_name='gobgpapi.FQDNCapability.domain_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1049,
  serialized_end=1153,
)


_UNKNOWNCAPABILITY = _descriptor.Descriptor(
  name='UnknownCapability',
  full_name='gobgpapi.UnknownCapability',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='gobgpapi.UnknownCapability.code', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='gobgpapi.UnknownCapability.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1155,
  serialized_end=1203,
)

_MULTIPROTOCOLCAPABILITY.fields_by_name['family'].message_type = gobgp__pb2._FAMILY
_EXTENDEDNEXTHOPCAPABILITYTUPLE.fields_by_name['nlri_family'].message_type = gobgp__pb2._FAMILY
_EXTENDEDNEXTHOPCAPABILITYTUPLE.fields_by_name['nexthop_family'].message_type = gobgp__pb2._FAMILY
_EXTENDEDNEXTHOPCAPABILITY.fields_by_name['tuples'].message_type = _EXTENDEDNEXTHOPCAPABILITYTUPLE
_GRACEFULRESTARTCAPABILITYTUPLE.fields_by_name['family'].message_type = gobgp__pb2._FAMILY
_GRACEFULRESTARTCAPABILITY.fields_by_name['tuples'].message_type = _GRACEFULRESTARTCAPABILITYTUPLE
_ADDPATHCAPABILITYTUPLE.fields_by_name['family'].message_type = gobgp__pb2._FAMILY
_ADDPATHCAPABILITYTUPLE.fields_by_name['mode'].enum_type = _ADDPATHMODE
_ADDPATHCAPABILITY.fields_by_name['tuples'].message_type = _ADDPATHCAPABILITYTUPLE
_LONGLIVEDGRACEFULRESTARTCAPABILITYTUPLE.fields_by_name['family'].message_type = gobgp__pb2._FAMILY
_LONGLIVEDGRACEFULRESTARTCAPABILITY.fields_by_name['tuples'].message_type = _LONGLIVEDGRACEFULRESTARTCAPABILITYTUPLE
DESCRIPTOR.message_types_by_name['MultiProtocolCapability'] = _MULTIPROTOCOLCAPABILITY
DESCRIPTOR.message_types_by_name['RouteRefreshCapability'] = _ROUTEREFRESHCAPABILITY
DESCRIPTOR.message_types_by_name['CarryingLabelInfoCapability'] = _CARRYINGLABELINFOCAPABILITY
DESCRIPTOR.message_types_by_name['ExtendedNexthopCapabilityTuple'] = _EXTENDEDNEXTHOPCAPABILITYTUPLE
DESCRIPTOR.message_types_by_name['ExtendedNexthopCapability'] = _EXTENDEDNEXTHOPCAPABILITY
DESCRIPTOR.message_types_by_name['GracefulRestartCapabilityTuple'] = _GRACEFULRESTARTCAPABILITYTUPLE
DESCRIPTOR.message_types_by_name['GracefulRestartCapability'] = _GRACEFULRESTARTCAPABILITY
DESCRIPTOR.message_types_by_name['FourOctetASNumberCapability'] = _FOUROCTETASNUMBERCAPABILITY
DESCRIPTOR.message_types_by_name['AddPathCapabilityTuple'] = _ADDPATHCAPABILITYTUPLE
DESCRIPTOR.message_types_by_name['AddPathCapability'] = _ADDPATHCAPABILITY
DESCRIPTOR.message_types_by_name['EnhancedRouteRefreshCapability'] = _ENHANCEDROUTEREFRESHCAPABILITY
DESCRIPTOR.message_types_by_name['LongLivedGracefulRestartCapabilityTuple'] = _LONGLIVEDGRACEFULRESTARTCAPABILITYTUPLE
DESCRIPTOR.message_types_by_name['LongLivedGracefulRestartCapability'] = _LONGLIVEDGRACEFULRESTARTCAPABILITY
DESCRIPTOR.message_types_by_name['RouteRefreshCiscoCapability'] = _ROUTEREFRESHCISCOCAPABILITY
DESCRIPTOR.message_types_by_name['FQDNCapability'] = _FQDNCAPABILITY
DESCRIPTOR.message_types_by_name['UnknownCapability'] = _UNKNOWNCAPABILITY
DESCRIPTOR.enum_types_by_name['AddPathMode'] = _ADDPATHMODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MultiProtocolCapability = _reflection.GeneratedProtocolMessageType('MultiProtocolCapability', (_message.Message,), {
  'DESCRIPTOR' : _MULTIPROTOCOLCAPABILITY,
  '__module__' : 'capability_pb2'
  # @@protoc_insertion_point(class_scope:gobgpapi.MultiProtocolCapability)
  })
_sym_db.RegisterMessage(MultiProtocolCapability)

RouteRefreshCapability = _reflection.GeneratedProtocolMessageType('RouteRefreshCapability', (_message.Message,), {
  'DESCRIPTOR' : _ROUTEREFRESHCAPABILITY,
  '__module__' : 'capability_pb2'
  # @@protoc_insertion_point(class_scope:gobgpapi.RouteRefreshCapability)
  })
_sym_db.RegisterMessage(RouteRefreshCapability)

CarryingLabelInfoCapability = _reflection.GeneratedProtocolMessageType('CarryingLabelInfoCapability', (_message.Message,), {
  'DESCRIPTOR' : _CARRYINGLABELINFOCAPABILITY,
  '__module__' : 'capability_pb2'
  # @@protoc_insertion_point(class_scope:gobgpapi.CarryingLabelInfoCapability)
  })
_sym_db.RegisterMessage(CarryingLabelInfoCapability)

ExtendedNexthopCapabilityTuple = _reflection.GeneratedProtocolMessageType('ExtendedNexthopCapabilityTuple', (_message.Message,), {
  'DESCRIPTOR' : _EXTENDEDNEXTHOPCAPABILITYTUPLE,
  '__module__' : 'capability_pb2'
  # @@protoc_insertion_point(class_scope:gobgpapi.ExtendedNexthopCapabilityTuple)
  })
_sym_db.RegisterMessage(ExtendedNexthopCapabilityTuple)

ExtendedNexthopCapability = _reflection.GeneratedProtocolMessageType('ExtendedNexthopCapability', (_message.Message,), {
  'DESCRIPTOR' : _EXTENDEDNEXTHOPCAPABILITY,
  '__module__' : 'capability_pb2'
  # @@protoc_insertion_point(class_scope:gobgpapi.ExtendedNexthopCapability)
  })
_sym_db.RegisterMessage(ExtendedNexthopCapability)

GracefulRestartCapabilityTuple = _reflection.GeneratedProtocolMessageType('GracefulRestartCapabilityTuple', (_message.Message,), {
  'DESCRIPTOR' : _GRACEFULRESTARTCAPABILITYTUPLE,
  '__module__' : 'capability_pb2'
  # @@protoc_insertion_point(class_scope:gobgpapi.GracefulRestartCapabilityTuple)
  })
_sym_db.RegisterMessage(GracefulRestartCapabilityTuple)

GracefulRestartCapability = _reflection.GeneratedProtocolMessageType('GracefulRestartCapability', (_message.Message,), {
  'DESCRIPTOR' : _GRACEFULRESTARTCAPABILITY,
  '__module__' : 'capability_pb2'
  # @@protoc_insertion_point(class_scope:gobgpapi.GracefulRestartCapability)
  })
_sym_db.RegisterMessage(GracefulRestartCapability)

FourOctetASNumberCapability = _reflection.GeneratedProtocolMessageType('FourOctetASNumberCapability', (_message.Message,), {
  'DESCRIPTOR' : _FOUROCTETASNUMBERCAPABILITY,
  '__module__' : 'capability_pb2'
  # @@protoc_insertion_point(class_scope:gobgpapi.FourOctetASNumberCapability)
  })
_sym_db.RegisterMessage(FourOctetASNumberCapability)

AddPathCapabilityTuple = _reflection.GeneratedProtocolMessageType('AddPathCapabilityTuple', (_message.Message,), {
  'DESCRIPTOR' : _ADDPATHCAPABILITYTUPLE,
  '__module__' : 'capability_pb2'
  # @@protoc_insertion_point(class_scope:gobgpapi.AddPathCapabilityTuple)
  })
_sym_db.RegisterMessage(AddPathCapabilityTuple)

AddPathCapability = _reflection.GeneratedProtocolMessageType('AddPathCapability', (_message.Message,), {
  'DESCRIPTOR' : _ADDPATHCAPABILITY,
  '__module__' : 'capability_pb2'
  # @@protoc_insertion_point(class_scope:gobgpapi.AddPathCapability)
  })
_sym_db.RegisterMessage(AddPathCapability)

EnhancedRouteRefreshCapability = _reflection.GeneratedProtocolMessageType('EnhancedRouteRefreshCapability', (_message.Message,), {
  'DESCRIPTOR' : _ENHANCEDROUTEREFRESHCAPABILITY,
  '__module__' : 'capability_pb2'
  # @@protoc_insertion_point(class_scope:gobgpapi.EnhancedRouteRefreshCapability)
  })
_sym_db.RegisterMessage(EnhancedRouteRefreshCapability)

LongLivedGracefulRestartCapabilityTuple = _reflection.GeneratedProtocolMessageType('LongLivedGracefulRestartCapabilityTuple', (_message.Message,), {
  'DESCRIPTOR' : _LONGLIVEDGRACEFULRESTARTCAPABILITYTUPLE,
  '__module__' : 'capability_pb2'
  # @@protoc_insertion_point(class_scope:gobgpapi.LongLivedGracefulRestartCapabilityTuple)
  })
_sym_db.RegisterMessage(LongLivedGracefulRestartCapabilityTuple)

LongLivedGracefulRestartCapability = _reflection.GeneratedProtocolMessageType('LongLivedGracefulRestartCapability', (_message.Message,), {
  'DESCRIPTOR' : _LONGLIVEDGRACEFULRESTARTCAPABILITY,
  '__module__' : 'capability_pb2'
  # @@protoc_insertion_point(class_scope:gobgpapi.LongLivedGracefulRestartCapability)
  })
_sym_db.RegisterMessage(LongLivedGracefulRestartCapability)

RouteRefreshCiscoCapability = _reflection.GeneratedProtocolMessageType('RouteRefreshCiscoCapability', (_message.Message,), {
  'DESCRIPTOR' : _ROUTEREFRESHCISCOCAPABILITY,
  '__module__' : 'capability_pb2'
  # @@protoc_insertion_point(class_scope:gobgpapi.RouteRefreshCiscoCapability)
  })
_sym_db.RegisterMessage(RouteRefreshCiscoCapability)

FQDNCapability = _reflection.GeneratedProtocolMessageType('FQDNCapability', (_message.Message,), {
  'DESCRIPTOR' : _FQDNCAPABILITY,
  '__module__' : 'capability_pb2'
  # @@protoc_insertion_point(class_scope:gobgpapi.FQDNCapability)
  })
_sym_db.RegisterMessage(FQDNCapability)

UnknownCapability = _reflection.GeneratedProtocolMessageType('UnknownCapability', (_message.Message,), {
  'DESCRIPTOR' : _UNKNOWNCAPABILITY,
  '__module__' : 'capability_pb2'
  # @@protoc_insertion_point(class_scope:gobgpapi.UnknownCapability)
  })
_sym_db.RegisterMessage(UnknownCapability)


# @@protoc_insertion_point(module_scope)
