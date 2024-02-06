from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FileReq(_message.Message):
    __slots__ = ("name", "mode")
    NAME_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    mode: str
    def __init__(self, name: _Optional[str] = ..., mode: _Optional[str] = ...) -> None: ...

class FileRes(_message.Message):
    __slots__ = ("status", "name")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    status: int
    name: str
    def __init__(self, status: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class ReadReq(_message.Message):
    __slots__ = ("chunk", "status", "name")
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    chunk: int
    status: int
    name: str
    def __init__(self, chunk: _Optional[int] = ..., status: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class ReadRes(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: str
    def __init__(self, data: _Optional[str] = ...) -> None: ...

class WriteReq(_message.Message):
    __slots__ = ("data", "name")
    DATA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    data: str
    name: str
    def __init__(self, data: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class WriteRes(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class LseekReq(_message.Message):
    __slots__ = ("offset", "name", "whence")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    WHENCE_FIELD_NUMBER: _ClassVar[int]
    offset: int
    name: str
    whence: int
    def __init__(self, offset: _Optional[int] = ..., name: _Optional[str] = ..., whence: _Optional[int] = ...) -> None: ...

class LseekRes(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class CloseReq(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CloseRes(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...
