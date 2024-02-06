import grpc
import nfs_pb2
import nfs_pb2_grpc
from concurrent import futures


class NFS_Servicer():
    def __init__(self) -> None:
        self.files = {}

    def Open(self, request, context):
        if(request.name in self.files):
            return nfs_pb2.FileRes(status=-1, name="FILE ALREADY OPEN")
        else:
            self.files[request.name] = [open(request.name, request.mode), request.mode]
            return nfs_pb2.FileRes(status=0, name="OPEN SUCCESS")

    def Create(self, request, context):
        if(request.name not in self.files):
            file = open(request.name, "w+")
            file.close()
            return nfs_pb2.FileRes(status=0, name="CREATE SUCCESS")

        else:
            return nfs_pb2.FileRes(status=0, name="CREATE FAILED")

    def Read(self, request, context):
        if(request.name not in self.files):
            return nfs_pb2.ReadRes(data="FILE NOT OPEN")
        
        if(self.files[request.name][1] == "w"):
            return nfs_pb2.ReadRes(data="WRONG MODE FOR FILE")

        file = self.files[request.name][0]
        data = file.read(request.chunk)
        return nfs_pb2.ReadRes(data=data)
    
    def Write(self, request, context):
        if(request.name not in self.files):
            return nfs_pb2.FileRes(status=-1, name="FILE NOT OPEN")
        
        if(self.files[request.name][1] == "r"):
            return nfs_pb2.FileRes(status=-1, name="WRONG MODE FOR FILE")

        file = self.files[request.name][0]
        file.write(request.data)
        return nfs_pb2.FileRes(status=2)
    
    def Lseek(self, request, context):
        if(request.name not in self.files):
            return nfs_pb2.FileRes(status=-1, name="FILE NOT OPEN")
        
        file = self.files[request.name][0]
        file.seek(request.offset, request.whence)
        return nfs_pb2.FileRes(status=3)
    
    def Close(self, request, context):
        try:
            file = self.files[request.name][0]
            file.close()
            del self.files[request.name]
            return nfs_pb2.CloseRes(status=4)
        except:
            return nfs_pb2.CloseRes(status=-1)

def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    nfs_pb2_grpc.add_NFSServicer_to_server(NFS_Servicer(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    serve()

