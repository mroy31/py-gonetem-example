from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StatusCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OK: _ClassVar[StatusCode]
    ERROR: _ClassVar[StatusCode]

class IfState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UP: _ClassVar[IfState]
    DOWN: _ClassVar[IfState]
OK: StatusCode
ERROR: StatusCode
UP: IfState
DOWN: IfState

class CopyMsg(_message.Message):
    __slots__ = ("code", "prjId", "node", "nodePath", "data")
    class Code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INIT: _ClassVar[CopyMsg.Code]
        DATA: _ClassVar[CopyMsg.Code]
        ERROR: _ClassVar[CopyMsg.Code]
    INIT: CopyMsg.Code
    DATA: CopyMsg.Code
    ERROR: CopyMsg.Code
    CODE_FIELD_NUMBER: _ClassVar[int]
    PRJID_FIELD_NUMBER: _ClassVar[int]
    NODE_FIELD_NUMBER: _ClassVar[int]
    NODEPATH_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    code: CopyMsg.Code
    prjId: str
    node: str
    nodePath: str
    data: bytes
    def __init__(self, code: _Optional[_Union[CopyMsg.Code, str]] = ..., prjId: _Optional[str] = ..., node: _Optional[str] = ..., nodePath: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...

class ConsoleCltMsg(_message.Message):
    __slots__ = ("code", "prjId", "node", "shell", "ttyWidth", "ttyHeight", "data")
    class Code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INIT: _ClassVar[ConsoleCltMsg.Code]
        DATA: _ClassVar[ConsoleCltMsg.Code]
        RESIZE: _ClassVar[ConsoleCltMsg.Code]
        CLOSE: _ClassVar[ConsoleCltMsg.Code]
    INIT: ConsoleCltMsg.Code
    DATA: ConsoleCltMsg.Code
    RESIZE: ConsoleCltMsg.Code
    CLOSE: ConsoleCltMsg.Code
    CODE_FIELD_NUMBER: _ClassVar[int]
    PRJID_FIELD_NUMBER: _ClassVar[int]
    NODE_FIELD_NUMBER: _ClassVar[int]
    SHELL_FIELD_NUMBER: _ClassVar[int]
    TTYWIDTH_FIELD_NUMBER: _ClassVar[int]
    TTYHEIGHT_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    code: ConsoleCltMsg.Code
    prjId: str
    node: str
    shell: bool
    ttyWidth: int
    ttyHeight: int
    data: bytes
    def __init__(self, code: _Optional[_Union[ConsoleCltMsg.Code, str]] = ..., prjId: _Optional[str] = ..., node: _Optional[str] = ..., shell: bool = ..., ttyWidth: _Optional[int] = ..., ttyHeight: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class ConsoleSrvMsg(_message.Message):
    __slots__ = ("code", "data")
    class Code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STDOUT: _ClassVar[ConsoleSrvMsg.Code]
        STDERR: _ClassVar[ConsoleSrvMsg.Code]
        ERROR: _ClassVar[ConsoleSrvMsg.Code]
        CLOSE: _ClassVar[ConsoleSrvMsg.Code]
    STDOUT: ConsoleSrvMsg.Code
    STDERR: ConsoleSrvMsg.Code
    ERROR: ConsoleSrvMsg.Code
    CLOSE: ConsoleSrvMsg.Code
    CODE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    code: ConsoleSrvMsg.Code
    data: bytes
    def __init__(self, code: _Optional[_Union[ConsoleSrvMsg.Code, str]] = ..., data: _Optional[bytes] = ...) -> None: ...

class PullSrvMsg(_message.Message):
    __slots__ = ("code", "image", "error")
    class Code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        START: _ClassVar[PullSrvMsg.Code]
        OK: _ClassVar[PullSrvMsg.Code]
        ERROR: _ClassVar[PullSrvMsg.Code]
    START: PullSrvMsg.Code
    OK: PullSrvMsg.Code
    ERROR: PullSrvMsg.Code
    CODE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    code: PullSrvMsg.Code
    image: str
    error: str
    def __init__(self, code: _Optional[_Union[PullSrvMsg.Code, str]] = ..., image: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...

class CaptureSrvMsg(_message.Message):
    __slots__ = ("code", "data")
    class Code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STDOUT: _ClassVar[CaptureSrvMsg.Code]
        STDERR: _ClassVar[CaptureSrvMsg.Code]
        OK: _ClassVar[CaptureSrvMsg.Code]
        ERROR: _ClassVar[CaptureSrvMsg.Code]
    STDOUT: CaptureSrvMsg.Code
    STDERR: CaptureSrvMsg.Code
    OK: CaptureSrvMsg.Code
    ERROR: CaptureSrvMsg.Code
    CODE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    code: CaptureSrvMsg.Code
    data: bytes
    def __init__(self, code: _Optional[_Union[CaptureSrvMsg.Code, str]] = ..., data: _Optional[bytes] = ...) -> None: ...

class TopologyRunMsg(_message.Message):
    __slots__ = ("code", "total", "nodeMessages")
    class Code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NODE_COUNT: _ClassVar[TopologyRunMsg.Code]
        BRIDGE_COUNT: _ClassVar[TopologyRunMsg.Code]
        LINK_COUNT: _ClassVar[TopologyRunMsg.Code]
        NODE_START: _ClassVar[TopologyRunMsg.Code]
        LINK_SETUP: _ClassVar[TopologyRunMsg.Code]
        BRIDGE_START: _ClassVar[TopologyRunMsg.Code]
        NODE_LOADCONFIG: _ClassVar[TopologyRunMsg.Code]
        NODE_MESSAGES: _ClassVar[TopologyRunMsg.Code]
        NODE_STOP: _ClassVar[TopologyRunMsg.Code]
        NODE_RM: _ClassVar[TopologyRunMsg.Code]
    NODE_COUNT: TopologyRunMsg.Code
    BRIDGE_COUNT: TopologyRunMsg.Code
    LINK_COUNT: TopologyRunMsg.Code
    NODE_START: TopologyRunMsg.Code
    LINK_SETUP: TopologyRunMsg.Code
    BRIDGE_START: TopologyRunMsg.Code
    NODE_LOADCONFIG: TopologyRunMsg.Code
    NODE_MESSAGES: TopologyRunMsg.Code
    NODE_STOP: TopologyRunMsg.Code
    NODE_RM: TopologyRunMsg.Code
    class NodeMessages(_message.Message):
        __slots__ = ("name", "messages")
        NAME_FIELD_NUMBER: _ClassVar[int]
        MESSAGES_FIELD_NUMBER: _ClassVar[int]
        name: str
        messages: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, name: _Optional[str] = ..., messages: _Optional[_Iterable[str]] = ...) -> None: ...
    CODE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    NODEMESSAGES_FIELD_NUMBER: _ClassVar[int]
    code: TopologyRunMsg.Code
    total: int
    nodeMessages: _containers.RepeatedCompositeFieldContainer[TopologyRunMsg.NodeMessages]
    def __init__(self, code: _Optional[_Union[TopologyRunMsg.Code, str]] = ..., total: _Optional[int] = ..., nodeMessages: _Optional[_Iterable[_Union[TopologyRunMsg.NodeMessages, _Mapping]]] = ...) -> None: ...

class ProjectSaveMsg(_message.Message):
    __slots__ = ("code", "data", "total")
    class Code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NODE_COUNT: _ClassVar[ProjectSaveMsg.Code]
        NODE_SAVE: _ClassVar[ProjectSaveMsg.Code]
        DATA: _ClassVar[ProjectSaveMsg.Code]
    NODE_COUNT: ProjectSaveMsg.Code
    NODE_SAVE: ProjectSaveMsg.Code
    DATA: ProjectSaveMsg.Code
    CODE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    code: ProjectSaveMsg.Code
    data: bytes
    total: int
    def __init__(self, code: _Optional[_Union[ProjectSaveMsg.Code, str]] = ..., data: _Optional[bytes] = ..., total: _Optional[int] = ...) -> None: ...

class ProjectCloseMsg(_message.Message):
    __slots__ = ("code", "total")
    class Code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NODE_COUNT: _ClassVar[ProjectCloseMsg.Code]
        BRIDGE_COUNT: _ClassVar[ProjectCloseMsg.Code]
        NODE_CLOSE: _ClassVar[ProjectCloseMsg.Code]
        BRIDGE_CLOSE: _ClassVar[ProjectCloseMsg.Code]
    NODE_COUNT: ProjectCloseMsg.Code
    BRIDGE_COUNT: ProjectCloseMsg.Code
    NODE_CLOSE: ProjectCloseMsg.Code
    BRIDGE_CLOSE: ProjectCloseMsg.Code
    CODE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    code: ProjectCloseMsg.Code
    total: int
    def __init__(self, code: _Optional[_Union[ProjectCloseMsg.Code, str]] = ..., total: _Optional[int] = ...) -> None: ...

class LinkConfig(_message.Message):
    __slots__ = ("peer1", "peer2", "loss", "delay", "jitter")
    PEER1_FIELD_NUMBER: _ClassVar[int]
    PEER2_FIELD_NUMBER: _ClassVar[int]
    LOSS_FIELD_NUMBER: _ClassVar[int]
    DELAY_FIELD_NUMBER: _ClassVar[int]
    JITTER_FIELD_NUMBER: _ClassVar[int]
    peer1: str
    peer2: str
    loss: float
    delay: int
    jitter: int
    def __init__(self, peer1: _Optional[str] = ..., peer2: _Optional[str] = ..., loss: _Optional[float] = ..., delay: _Optional[int] = ..., jitter: _Optional[int] = ...) -> None: ...

class LinkRequest(_message.Message):
    __slots__ = ("prjId", "link")
    PRJID_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    prjId: str
    link: LinkConfig
    def __init__(self, prjId: _Optional[str] = ..., link: _Optional[_Union[LinkConfig, _Mapping]] = ...) -> None: ...

class NodeIfStateRequest(_message.Message):
    __slots__ = ("prjId", "node", "ifIndex", "state")
    PRJID_FIELD_NUMBER: _ClassVar[int]
    NODE_FIELD_NUMBER: _ClassVar[int]
    IFINDEX_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    prjId: str
    node: str
    ifIndex: int
    state: IfState
    def __init__(self, prjId: _Optional[str] = ..., node: _Optional[str] = ..., ifIndex: _Optional[int] = ..., state: _Optional[_Union[IfState, str]] = ...) -> None: ...

class NodeInterfaceRequest(_message.Message):
    __slots__ = ("prjId", "node", "ifIndex")
    PRJID_FIELD_NUMBER: _ClassVar[int]
    NODE_FIELD_NUMBER: _ClassVar[int]
    IFINDEX_FIELD_NUMBER: _ClassVar[int]
    prjId: str
    node: str
    ifIndex: int
    def __init__(self, prjId: _Optional[str] = ..., node: _Optional[str] = ..., ifIndex: _Optional[int] = ...) -> None: ...

class NodeRequest(_message.Message):
    __slots__ = ("prjId", "node")
    PRJID_FIELD_NUMBER: _ClassVar[int]
    NODE_FIELD_NUMBER: _ClassVar[int]
    prjId: str
    node: str
    def __init__(self, prjId: _Optional[str] = ..., node: _Optional[str] = ...) -> None: ...

class ProjectRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class WNetworkRequest(_message.Message):
    __slots__ = ("id", "data")
    ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    data: bytes
    def __init__(self, id: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...

class OpenRequest(_message.Message):
    __slots__ = ("name", "data")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    data: bytes
    def __init__(self, name: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...

class Status(_message.Message):
    __slots__ = ("code", "error")
    CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    code: StatusCode
    error: str
    def __init__(self, code: _Optional[_Union[StatusCode, str]] = ..., error: _Optional[str] = ...) -> None: ...

class AckResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class FileResponse(_message.Message):
    __slots__ = ("status", "data")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    status: Status
    data: bytes
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., data: _Optional[bytes] = ...) -> None: ...

class VersionResponse(_message.Message):
    __slots__ = ("status", "version")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    status: Status
    version: str
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., version: _Optional[str] = ...) -> None: ...

class StatusResponse(_message.Message):
    __slots__ = ("status", "name", "id", "openAt", "running", "nodes")
    class IfStatus(_message.Message):
        __slots__ = ("name", "state")
        NAME_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        name: str
        state: IfState
        def __init__(self, name: _Optional[str] = ..., state: _Optional[_Union[IfState, str]] = ...) -> None: ...
    class NodeStatus(_message.Message):
        __slots__ = ("name", "running", "interfaces")
        NAME_FIELD_NUMBER: _ClassVar[int]
        RUNNING_FIELD_NUMBER: _ClassVar[int]
        INTERFACES_FIELD_NUMBER: _ClassVar[int]
        name: str
        running: bool
        interfaces: _containers.RepeatedCompositeFieldContainer[StatusResponse.IfStatus]
        def __init__(self, name: _Optional[str] = ..., running: bool = ..., interfaces: _Optional[_Iterable[_Union[StatusResponse.IfStatus, _Mapping]]] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    OPENAT_FIELD_NUMBER: _ClassVar[int]
    RUNNING_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    status: Status
    name: str
    id: str
    openAt: str
    running: bool
    nodes: _containers.RepeatedCompositeFieldContainer[StatusResponse.NodeStatus]
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., name: _Optional[str] = ..., id: _Optional[str] = ..., openAt: _Optional[str] = ..., running: bool = ..., nodes: _Optional[_Iterable[_Union[StatusResponse.NodeStatus, _Mapping]]] = ...) -> None: ...

class ConfigFilesResponse(_message.Message):
    __slots__ = ("status", "source", "files")
    class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ARCHIVE: _ClassVar[ConfigFilesResponse.Source]
        RUNNING: _ClassVar[ConfigFilesResponse.Source]
    ARCHIVE: ConfigFilesResponse.Source
    RUNNING: ConfigFilesResponse.Source
    class ConfigFile(_message.Message):
        __slots__ = ("name", "data")
        NAME_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        name: str
        data: bytes
        def __init__(self, name: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    status: Status
    source: ConfigFilesResponse.Source
    files: _containers.RepeatedCompositeFieldContainer[ConfigFilesResponse.ConfigFile]
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., source: _Optional[_Union[ConfigFilesResponse.Source, str]] = ..., files: _Optional[_Iterable[_Union[ConfigFilesResponse.ConfigFile, _Mapping]]] = ...) -> None: ...

class PrjListResponse(_message.Message):
    __slots__ = ("status", "projects")
    class Info(_message.Message):
        __slots__ = ("id", "name", "openAt")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        OPENAT_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        openAt: str
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., openAt: _Optional[str] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PROJECTS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    projects: _containers.RepeatedCompositeFieldContainer[PrjListResponse.Info]
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., projects: _Optional[_Iterable[_Union[PrjListResponse.Info, _Mapping]]] = ...) -> None: ...

class PrjOpenResponse(_message.Message):
    __slots__ = ("status", "id")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    status: Status
    id: str
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...
