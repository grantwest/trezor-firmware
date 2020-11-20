# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .StellarAssetType import StellarAssetType

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class StellarChangeTrustOp(p.MessageType):
    MESSAGE_WIRE_TYPE = 216

    def __init__(
        self,
        *,
        source_account: str = None,
        asset: StellarAssetType = None,
        limit: int = None,
    ) -> None:
        super().__init__()
        self.source_account = source_account
        self.asset = asset
        self.limit = limit

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('source_account', p.UnicodeType, None),
            2: ('asset', StellarAssetType, None),
            3: ('limit', p.UVarintType, None),
        }
