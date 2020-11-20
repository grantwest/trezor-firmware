# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class EosActionUnknown(p.MessageType):

    def __init__(
        self,
        *,
        data_size: int = None,
        data_chunk: bytes = None,
    ) -> None:
        super().__init__()
        self.data_size = data_size
        self.data_chunk = data_chunk

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('data_size', p.UVarintType, None),
            2: ('data_chunk', p.BytesType, None),
        }
