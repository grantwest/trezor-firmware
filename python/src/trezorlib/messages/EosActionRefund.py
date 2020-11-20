# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class EosActionRefund(p.MessageType):

    def __init__(
        self,
        *,
        owner: int = None,
    ) -> None:
        super().__init__()
        self.owner = owner

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('owner', p.UVarintType, None),
        }
