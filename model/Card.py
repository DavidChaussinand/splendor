import dataclasses

from model.Cost import Cost


@dataclasses.dataclass
class Card:
    cost: Cost
