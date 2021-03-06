import grpc
import quran.endpoints.grpc.entity_pb2 as entity_proto
import quran.endpoints.grpc.shared_pb2 as shared_entity
import quran.endpoints.grpc.image_pb2_grpc as image_rpc


channel = grpc.insecure_channel("localhost:50051")
stub = image_rpc.ImageStub(channel)


def test_create_image():
    image = entity_proto.ImageEntity(ayah_id='ayah-1', image='link to image')
    res = stub.CreateImage(image)

    assert res.data.image.ayah_id == image.ayah_id
    assert res.data.image.image == image.image


def test_find_image_by_ayah_id():
    res = stub.FindImageByAyahId(shared_entity.IDRequest(id='ayah-1'))

    assert res.data.image.ayah_id == 'ayah-1'
    assert res.data.image.image == 'link to image'
