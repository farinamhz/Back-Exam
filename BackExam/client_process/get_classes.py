import grpc
from grpc_pb2s import class_pb2, class_pb2_grpc
from BackExam.settings import GOLESTAN_SYSTEM_URL

def get_classes(id:int):
    with grpc.insecure_channel(GOLESTAN_SYSTEM_URL) as channel:
        stub = class_pb2_grpc.ClassControllerStub(channel)
        user_id = class_pb2.ClassListRequest(user_id=id)
        classes = stub.List(user_id)
        return list(classes.class_id)

def get_common_classes(id:str):
    with grpc.insecure_channel(GOLESTAN_SYSTEM_URL) as channel:
        stub = class_pb2_grpc.ClassControllerStub(channel)
        class_id = class_pb2.ClassId(class_id=id)
        classes = stub.GetCommonClasses(class_id)
        return list(classes.class_id)

def is_exist(id:str):
    with grpc.insecure_channel(GOLESTAN_SYSTEM_URL) as channel:
        stub = class_pb2_grpc.ClassControllerStub(channel)
        class_id = class_pb2.ClassId(class_id=id)
        value = stub.IsExist(class_id)
        return value.is_exist

        