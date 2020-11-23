# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class DebugMoneroDiagRequest(p.MessageType):
    MESSAGE_WIRE_TYPE = 546

    def __init__(
        self,
        *,
        pd: List[int] = None,
        ins: int = None,
        p1: int = None,
        p2: int = None,
        data1: bytes = None,
        data2: bytes = None,
    ) -> None:
        self.pd = pd if pd is not None else []
        self.ins = ins
        self.p1 = p1
        self.p2 = p2
        self.data1 = data1
        self.data2 = data2

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('ins', p.UVarintType, None),
            2: ('p1', p.UVarintType, None),
            3: ('p2', p.UVarintType, None),
            4: ('pd', p.UVarintType, p.FLAG_REPEATED),
            5: ('data1', p.BytesType, None),
            6: ('data2', p.BytesType, None),
        }
