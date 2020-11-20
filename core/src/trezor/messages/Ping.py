# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class Ping(p.MessageType):
    MESSAGE_WIRE_TYPE = 1

    def __init__(
        self,
        *,
        message: str = None,
        button_protection: bool = None,
    ) -> None:
        super().__init__()
        self.message = message
        self.button_protection = button_protection

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('message', p.UnicodeType, None),
            2: ('button_protection', p.BoolType, None),
        }
