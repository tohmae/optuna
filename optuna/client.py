from optuna.protobuf import study_pb2
from optuna.protobuf import study_pb2_grpc
import grpc

class Client(object):
    def __init__(self):
        self.channel = grpc.insecure_channel('localhost:50051')

    def create_study(self, storage=None):
        stub = study_pb2_grpc.StudyStub(self.channel)
        options = study_pb2.CreateStudyOptions(storage=storage)
        return stub.create_study(options)

    def close_study(self, study):
        stub = study_pb2_grpc.StudyStub(self.channel)
        stub.close_study(study)

    def start_trial(self, study):
        stub = study_pb2_grpc.StudyStub(self.channel)
        return stub.start_trial(study)
