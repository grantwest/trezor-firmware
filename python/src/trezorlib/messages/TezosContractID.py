# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
        EnumTypeTezosContractType = Literal[0, 1]
    except ImportError:
        pass


class TezosContractID(p.MessageType):

    def __init__(
        self,
        *,
        tag: EnumTypeTezosContractType = None,
        hash: bytes = None,
    ) -> None:
        self.tag = tag
        self.hash = hash

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('tag', p.EnumType("TezosContractType", (0, 1)), None),
            2: ('hash', p.BytesType, None),
        }
