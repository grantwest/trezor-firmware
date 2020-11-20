# Automatically generated by pb2py
# fmt: off
import protobuf as p

from .TxInput import TxInput

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class TxAckInputWrapper(p.MessageType):

    def __init__(
        self,
        *,
        input: TxInput,
    ) -> None:
        super().__init__()
        self.input = input

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            2: ('input', TxInput, p.FLAG_REQUIRED),
        }
