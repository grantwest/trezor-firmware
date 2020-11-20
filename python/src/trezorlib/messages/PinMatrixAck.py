# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class PinMatrixAck(p.MessageType):
    MESSAGE_WIRE_TYPE = 19

    def __init__(
        self,
        *,
        pin: str,
    ) -> None:
        super().__init__()
        self.pin = pin

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('pin', p.UnicodeType, p.FLAG_REQUIRED),
        }
