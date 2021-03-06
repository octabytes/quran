# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import quran.endpoints.grpc.entity_pb2 as entity__pb2
import quran.endpoints.grpc.shared_pb2 as shared__pb2
import quran.endpoints.grpc.translation_pb2 as translation__pb2


class TranslationStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateTranslation = channel.unary_unary(
        '/quran.Translation/CreateTranslation',
        request_serializer=entity__pb2.TranslationEntity.SerializeToString,
        response_deserializer=translation__pb2.TranslationSingleResponse.FromString,
        )
    self.FindTranslationById = channel.unary_unary(
        '/quran.Translation/FindTranslationById',
        request_serializer=shared__pb2.IDRequest.SerializeToString,
        response_deserializer=translation__pb2.TranslationSingleResponse.FromString,
        )
    self.FindTranslationByAyahId = channel.unary_unary(
        '/quran.Translation/FindTranslationByAyahId',
        request_serializer=shared__pb2.IDRequest.SerializeToString,
        response_deserializer=translation__pb2.TranslationMultiResponse.FromString,
        )
    self.FindTranslationByEditionId = channel.unary_unary(
        '/quran.Translation/FindTranslationByEditionId',
        request_serializer=shared__pb2.IDRequest.SerializeToString,
        response_deserializer=translation__pb2.TranslationMultiResponse.FromString,
        )
    self.FilterTranslation = channel.unary_unary(
        '/quran.Translation/FilterTranslation',
        request_serializer=shared__pb2.FilterRequest.SerializeToString,
        response_deserializer=translation__pb2.TranslationSingleResponse.FromString,
        )


class TranslationServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def CreateTranslation(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FindTranslationById(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FindTranslationByAyahId(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FindTranslationByEditionId(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FilterTranslation(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TranslationServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateTranslation': grpc.unary_unary_rpc_method_handler(
          servicer.CreateTranslation,
          request_deserializer=entity__pb2.TranslationEntity.FromString,
          response_serializer=translation__pb2.TranslationSingleResponse.SerializeToString,
      ),
      'FindTranslationById': grpc.unary_unary_rpc_method_handler(
          servicer.FindTranslationById,
          request_deserializer=shared__pb2.IDRequest.FromString,
          response_serializer=translation__pb2.TranslationSingleResponse.SerializeToString,
      ),
      'FindTranslationByAyahId': grpc.unary_unary_rpc_method_handler(
          servicer.FindTranslationByAyahId,
          request_deserializer=shared__pb2.IDRequest.FromString,
          response_serializer=translation__pb2.TranslationMultiResponse.SerializeToString,
      ),
      'FindTranslationByEditionId': grpc.unary_unary_rpc_method_handler(
          servicer.FindTranslationByEditionId,
          request_deserializer=shared__pb2.IDRequest.FromString,
          response_serializer=translation__pb2.TranslationMultiResponse.SerializeToString,
      ),
      'FilterTranslation': grpc.unary_unary_rpc_method_handler(
          servicer.FilterTranslation,
          request_deserializer=shared__pb2.FilterRequest.FromString,
          response_serializer=translation__pb2.TranslationSingleResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'quran.Translation', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
