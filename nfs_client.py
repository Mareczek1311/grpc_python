

import grpc
import nfs_pb2
import nfs_pb2_grpc

def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = nfs_pb2_grpc.NFSStub(channel)
        
        print("Enter option: ")
        print("1. Open")
        print("2. Create")
        print("3. Read")
        print("4. Write")
        print("5. Lseek")
        print("6. Close")

        option = input()
        name = input("Enter file name: ")
        if(option == "1"):
            mode = input("Enter mode: ")
            response = stub.Open(nfs_pb2.FileReq(name=name, mode=mode))
            print(response.name)
        if(option == "2"):
            response = stub.Create(nfs_pb2.FileReq(name=name))
            print(response.name)
        if(option == "3"):
            chunk = int(input("Enter chunk size: "))
            response = stub.Read(nfs_pb2.ReadReq(name=name, chunk=chunk))
            print(response.data)
        if(option == "4"):
            data = input("Enter data: ")
            response = stub.Write(nfs_pb2.WriteReq(name=name, data=data))
            print(response.status)
        if(option == "5"):
            offset = int(input("Enter offset: "))
            whence = int(input("Enter whence: "))
            response = stub.Lseek(nfs_pb2.LseekReq(name=name, offset=offset, whence=whence))
            print(response.status)
        if(option == "6"):
            response = stub.Close(nfs_pb2.CloseReq(name=name))
            print(response.status)

if __name__ == '__main__':
    run()

