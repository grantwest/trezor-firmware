# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class OwnershipId(p.MessageType):
    MESSAGE_WIRE_TYPE = 44

    def __init__(
        self,
        *,
        ownership_id: bytes,
    ) -> None:
        super().__init__()
        self.ownership_id = ownership_id

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('ownership_id', p.BytesType, p.FLAG_REQUIRED),
        }
