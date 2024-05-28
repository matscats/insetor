from api.insetor.models.sector import Sector
from api.insetor.transports.sector import SectorTransport
import uuid
import typing
from django.shortcuts import get_object_or_404


class Sectors:
    @staticmethod
    def _make_transport(obj: Sector) -> SectorTransport:
        return SectorTransport(id=obj.id, name=obj.name, code=obj.code)

    @staticmethod
    def get_sector(sector_id: uuid.UUID) -> SectorTransport:
        sector = get_object_or_404(Sector, id=sector_id)
        return Sectors._make_transport(sector)

    @staticmethod
    def get_all_sectors() -> typing.Sequence[SectorTransport]:
        sectors = Sector.objects.all()
        return [Sectors._make_transport(sector) for sector in sectors]
