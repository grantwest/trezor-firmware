# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class EosSignedTx(p.MessageType):
    MESSAGE_WIRE_TYPE = 605

    def __init__(
        self,
        *,
        signature: str = None,
    ) -> None:
        super().__init__()
        self.signature = signature

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('signature', p.UnicodeType, None),
        }
