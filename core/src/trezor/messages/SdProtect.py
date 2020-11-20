# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
        EnumTypeSdProtectOperationType = Literal[0, 1, 2]
    except ImportError:
        pass


class SdProtect(p.MessageType):
    MESSAGE_WIRE_TYPE = 79

    def __init__(
        self,
        *,
        operation: EnumTypeSdProtectOperationType = None,
    ) -> None:
        super().__init__()
        self.operation = operation

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('operation', p.EnumType("SdProtectOperationType", (0, 1, 2)), None),
        }
