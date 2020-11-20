# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class FirmwareUpload(p.MessageType):
    MESSAGE_WIRE_TYPE = 7

    def __init__(
        self,
        *,
        payload: bytes,
        hash: bytes = None,
    ) -> None:
        super().__init__()
        self.payload = payload
        self.hash = hash

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('payload', p.BytesType, p.FLAG_REQUIRED),
            2: ('hash', p.BytesType, None),
        }
