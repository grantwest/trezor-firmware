# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class CardanoPoolMetadataType(p.MessageType):

    def __init__(
        self,
        *,
        url: str,
        hash: bytes,
    ) -> None:
        super().__init__()
        self.url = url
        self.hash = hash

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('url', p.UnicodeType, p.FLAG_REQUIRED),
            2: ('hash', p.BytesType, p.FLAG_REQUIRED),
        }
