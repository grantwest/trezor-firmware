# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
        EnumTypeInputScriptType = Literal[0, 1, 2, 3, 4]
    except ImportError:
        pass


class AuthorizeCoinJoin(p.MessageType):
    MESSAGE_WIRE_TYPE = 51
    UNSTABLE = True

    def __init__(
        self,
        *,
        coordinator: str,
        max_total_fee: int,
        address_n: List[int] = None,
        fee_per_anonymity: int = None,
        coin_name: str = "Bitcoin",
        script_type: EnumTypeInputScriptType = 0,
    ) -> None:
        super().__init__()
        self.address_n = address_n if address_n is not None else []
        self.coordinator = coordinator
        self.max_total_fee = max_total_fee
        self.fee_per_anonymity = fee_per_anonymity
        self.coin_name = coin_name
        self.script_type = script_type

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('coordinator', p.UnicodeType, p.FLAG_REQUIRED),
            2: ('max_total_fee', p.UVarintType, p.FLAG_REQUIRED),
            3: ('fee_per_anonymity', p.UVarintType, None),
            4: ('address_n', p.UVarintType, p.FLAG_REPEATED),
            5: ('coin_name', p.UnicodeType, "Bitcoin"),  # default=Bitcoin
            6: ('script_type', p.EnumType("InputScriptType", (0, 1, 2, 3, 4)), 0),  # default=SPENDADDRESS
        }
