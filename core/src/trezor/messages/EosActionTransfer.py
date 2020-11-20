# Automatically generated by pb2py
# fmt: off
import protobuf as p

from .EosAsset import EosAsset

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class EosActionTransfer(p.MessageType):

    def __init__(
        self,
        *,
        sender: int = None,
        receiver: int = None,
        quantity: EosAsset = None,
        memo: str = None,
    ) -> None:
        super().__init__()
        self.sender = sender
        self.receiver = receiver
        self.quantity = quantity
        self.memo = memo

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('sender', p.UVarintType, None),
            2: ('receiver', p.UVarintType, None),
            3: ('quantity', EosAsset, None),
            4: ('memo', p.UnicodeType, None),
        }
