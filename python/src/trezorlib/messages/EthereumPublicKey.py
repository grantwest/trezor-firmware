# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .HDNodeType import HDNodeType

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class EthereumPublicKey(p.MessageType):
    MESSAGE_WIRE_TYPE = 451

    def __init__(
        self,
        *,
        node: HDNodeType = None,
        xpub: str = None,
    ) -> None:
        super().__init__()
        self.node = node
        self.xpub = xpub

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('node', HDNodeType, None),
            2: ('xpub', p.UnicodeType, None),
        }
