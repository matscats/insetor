from dataclasses import dataclass
import uuid


@dataclass(frozen=True)
class SectorTransport:
    id: uuid.UUID
    name: str
    code: int
