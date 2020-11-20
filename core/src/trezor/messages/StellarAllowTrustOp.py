# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class StellarAllowTrustOp(p.MessageType):
    MESSAGE_WIRE_TYPE = 217

    def __init__(
        self,
        *,
        source_account: str = None,
        trusted_account: str = None,
        asset_type: int = None,
        asset_code: str = None,
        is_authorized: int = None,
    ) -> None:
        super().__init__()
        self.source_account = source_account
        self.trusted_account = trusted_account
        self.asset_type = asset_type
        self.asset_code = asset_code
        self.is_authorized = is_authorized

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('source_account', p.UnicodeType, None),
            2: ('trusted_account', p.UnicodeType, None),
            3: ('asset_type', p.UVarintType, None),
            4: ('asset_code', p.UnicodeType, None),
            5: ('is_authorized', p.UVarintType, None),
        }
