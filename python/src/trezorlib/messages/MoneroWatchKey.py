# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class MoneroWatchKey(p.MessageType):
    MESSAGE_WIRE_TYPE = 543

    def __init__(
        self,
        *,
        watch_key: bytes = None,
        address: bytes = None,
    ) -> None:
        super().__init__()
        self.watch_key = watch_key
        self.address = address

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('watch_key', p.BytesType, None),
            2: ('address', p.BytesType, None),
        }
