# Automatically generated by pb2py
# fmt: off
import protobuf as p

from .IdentityType import IdentityType

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class GetECDHSessionKey(p.MessageType):
    MESSAGE_WIRE_TYPE = 61

    def __init__(
        self,
        *,
        identity: IdentityType = None,
        peer_public_key: bytes = None,
        ecdsa_curve_name: str = None,
    ) -> None:
        super().__init__()
        self.identity = identity
        self.peer_public_key = peer_public_key
        self.ecdsa_curve_name = ecdsa_curve_name

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('identity', IdentityType, None),
            2: ('peer_public_key', p.BytesType, None),
            3: ('ecdsa_curve_name', p.UnicodeType, None),
        }
