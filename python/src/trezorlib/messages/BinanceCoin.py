# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class BinanceCoin(p.MessageType):

    def __init__(
        self,
        *,
        amount: int = None,
        denom: str = None,
    ) -> None:
        super().__init__()
        self.amount = amount
        self.denom = denom

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('amount', p.SVarintType, None),
            2: ('denom', p.UnicodeType, None),
        }
