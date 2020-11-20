# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class OwnershipProof(p.MessageType):
    MESSAGE_WIRE_TYPE = 50

    def __init__(
        self,
        *,
        ownership_proof: bytes,
        signature: bytes,
    ) -> None:
        super().__init__()
        self.ownership_proof = ownership_proof
        self.signature = signature

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('ownership_proof', p.BytesType, p.FLAG_REQUIRED),
            2: ('signature', p.BytesType, p.FLAG_REQUIRED),
        }
