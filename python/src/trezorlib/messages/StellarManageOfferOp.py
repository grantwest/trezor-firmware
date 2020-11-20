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


class StellarManageOfferOp(p.MessageType):
    MESSAGE_WIRE_TYPE = 213

    def __init__(
        self,
        *,
        source_account: str = None,
        selling_asset: StellarAssetType = None,
        buying_asset: StellarAssetType = None,
        amount: int = None,
        price_n: int = None,
        price_d: int = None,
        offer_id: int = None,
    ) -> None:
        super().__init__()
        self.source_account = source_account
        self.selling_asset = selling_asset
        self.buying_asset = buying_asset
        self.amount = amount
        self.price_n = price_n
        self.price_d = price_d
        self.offer_id = offer_id

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('source_account', p.UnicodeType, None),
            2: ('selling_asset', StellarAssetType, None),
            3: ('buying_asset', StellarAssetType, None),
            4: ('amount', p.SVarintType, None),
            5: ('price_n', p.UVarintType, None),
            6: ('price_d', p.UVarintType, None),
            7: ('offer_id', p.UVarintType, None),
        }
