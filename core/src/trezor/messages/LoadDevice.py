# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class LoadDevice(p.MessageType):
    MESSAGE_WIRE_TYPE = 13

    def __init__(
        self,
        *,
        mnemonics: List[str] = None,
        pin: str = None,
        passphrase_protection: bool = None,
        language: str = "en-US",
        label: str = None,
        skip_checksum: bool = None,
        u2f_counter: int = None,
        needs_backup: bool = None,
        no_backup: bool = None,
    ) -> None:
        super().__init__()
        self.mnemonics = mnemonics if mnemonics is not None else []
        self.pin = pin
        self.passphrase_protection = passphrase_protection
        self.language = language
        self.label = label
        self.skip_checksum = skip_checksum
        self.u2f_counter = u2f_counter
        self.needs_backup = needs_backup
        self.no_backup = no_backup

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('mnemonics', p.UnicodeType, p.FLAG_REPEATED),
            3: ('pin', p.UnicodeType, None),
            4: ('passphrase_protection', p.BoolType, None),
            5: ('language', p.UnicodeType, "en-US"),  # default=en-US
            6: ('label', p.UnicodeType, None),
            7: ('skip_checksum', p.BoolType, None),
            8: ('u2f_counter', p.UVarintType, None),
            9: ('needs_backup', p.BoolType, None),
            10: ('no_backup', p.BoolType, None),
        }
