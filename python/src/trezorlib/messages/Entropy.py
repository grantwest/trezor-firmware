# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class Entropy(p.MessageType):
    MESSAGE_WIRE_TYPE = 10

    def __init__(
        self,
        *,
        entropy: bytes,
    ) -> None:
        super().__init__()
        self.entropy = entropy

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('entropy', p.BytesType, p.FLAG_REQUIRED),
        }
