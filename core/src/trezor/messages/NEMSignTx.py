# Automatically generated by pb2py
# fmt: off
import protobuf as p

from .NEMAggregateModification import NEMAggregateModification
from .NEMImportanceTransfer import NEMImportanceTransfer
from .NEMMosaicCreation import NEMMosaicCreation
from .NEMMosaicSupplyChange import NEMMosaicSupplyChange
from .NEMProvisionNamespace import NEMProvisionNamespace
from .NEMTransactionCommon import NEMTransactionCommon
from .NEMTransfer import NEMTransfer

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class NEMSignTx(p.MessageType):
    MESSAGE_WIRE_TYPE = 69

    def __init__(
        self,
        *,
        transaction: NEMTransactionCommon = None,
        multisig: NEMTransactionCommon = None,
        transfer: NEMTransfer = None,
        cosigning: bool = None,
        provision_namespace: NEMProvisionNamespace = None,
        mosaic_creation: NEMMosaicCreation = None,
        supply_change: NEMMosaicSupplyChange = None,
        aggregate_modification: NEMAggregateModification = None,
        importance_transfer: NEMImportanceTransfer = None,
    ) -> None:
        super().__init__()
        self.transaction = transaction
        self.multisig = multisig
        self.transfer = transfer
        self.cosigning = cosigning
        self.provision_namespace = provision_namespace
        self.mosaic_creation = mosaic_creation
        self.supply_change = supply_change
        self.aggregate_modification = aggregate_modification
        self.importance_transfer = importance_transfer

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('transaction', NEMTransactionCommon, None),
            2: ('multisig', NEMTransactionCommon, None),
            3: ('transfer', NEMTransfer, None),
            4: ('cosigning', p.BoolType, None),
            5: ('provision_namespace', NEMProvisionNamespace, None),
            6: ('mosaic_creation', NEMMosaicCreation, None),
            7: ('supply_change', NEMMosaicSupplyChange, None),
            8: ('aggregate_modification', NEMAggregateModification, None),
            9: ('importance_transfer', NEMImportanceTransfer, None),
        }
