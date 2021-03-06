import grpc
import quran.endpoints.grpc.entity_pb2 as entity_proto
import quran.endpoints.grpc.shared_pb2 as shared_entity
import quran.endpoints.grpc.translation_pb2_grpc as translation_rpc
from quran.utils.proto_converter import ProtoConverter

channel = grpc.insecure_channel("localhost:50051")
stub = translation_rpc.TranslationStub(channel)


def test_create_translation():
    translation = entity_proto.TranslationEntity(id='translation-1', ayah_id='ayah-1', edition_id='edition-1',
                                                 text='translation text')

    res = stub.CreateTranslation(translation)

    assert ProtoConverter.proto_to_dict(res.data.translation) == ProtoConverter.proto_to_dict(translation)


def test_find_translation_by_id():
    res = stub.FindTranslationById(shared_entity.IDRequest(id='translation-1'))

    assert res.data.translation.id == 'translation-1'


def test_find_translation_by_ayah_id():
    translation_stream = stub.FindTranslationByAyahId(shared_entity.IDRequest(id='ayah-1'))

    for translation in translation_stream.data.translation:
        assert translation.ayah_id == 'ayah-1'


def test_find_translation_by_edition_id():
    translation_stream = stub.FindTranslationByEditionId(shared_entity.IDRequest(id='edition-1'))

    for translation in translation_stream.data.translation:
        assert translation.edition_id == 'edition-1'


def test_filter_translation():
    res = stub.FilterTranslation(shared_entity.FilterRequest(ayah_id='ayah-1', edition_id='edition-1'))

    assert res.data.translation.ayah_id == 'ayah-1'
    assert res.data.translation.edition_id == 'edition-1'
