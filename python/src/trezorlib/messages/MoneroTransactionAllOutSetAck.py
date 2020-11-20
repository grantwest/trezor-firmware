# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .MoneroRingCtSig import MoneroRingCtSig

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class MoneroTransactionAllOutSetAck(p.MessageType):
    MESSAGE_WIRE_TYPE = 514

    def __init__(
        self,
        *,
        extra: bytes = None,
        tx_prefix_hash: bytes = None,
        rv: MoneroRingCtSig = None,
        full_message_hash: bytes = None,
    ) -> None:
        super().__init__()
        self.extra = extra
        self.tx_prefix_hash = tx_prefix_hash
        self.rv = rv
        self.full_message_hash = full_message_hash

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('extra', p.BytesType, None),
            2: ('tx_prefix_hash', p.BytesType, None),
            4: ('rv', MoneroRingCtSig, None),
            5: ('full_message_hash', p.BytesType, None),
        }
