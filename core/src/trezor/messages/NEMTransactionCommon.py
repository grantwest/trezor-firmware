# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class NEMTransactionCommon(p.MessageType):

    def __init__(
        self,
        *,
        address_n: List[int] = None,
        network: int = None,
        timestamp: int = None,
        fee: int = None,
        deadline: int = None,
        signer: bytes = None,
    ) -> None:
        super().__init__()
        self.address_n = address_n if address_n is not None else []
        self.network = network
        self.timestamp = timestamp
        self.fee = fee
        self.deadline = deadline
        self.signer = signer

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('address_n', p.UVarintType, p.FLAG_REPEATED),
            2: ('network', p.UVarintType, None),
            3: ('timestamp', p.UVarintType, None),
            4: ('fee', p.UVarintType, None),
            5: ('deadline', p.UVarintType, None),
            6: ('signer', p.BytesType, None),
        }
