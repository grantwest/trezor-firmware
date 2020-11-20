# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .MoneroRctKeyPublic import MoneroRctKeyPublic

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class MoneroOutputEntry(p.MessageType):

    def __init__(
        self,
        *,
        idx: int = None,
        key: MoneroRctKeyPublic = None,
    ) -> None:
        super().__init__()
        self.idx = idx
        self.key = key

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('idx', p.UVarintType, None),
            2: ('key', MoneroRctKeyPublic, None),
        }
