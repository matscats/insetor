from api.insetor.transports.sector import SectorTransport
from dataclasses import dataclass
import uuid


@dataclass(frozen=True)
class EmployeeTransport:
    id: uuid.UUID
    name: str
    sector: SectorTransport
