from django.views import View
from django.http.response import JsonResponse
from api.insetor.services.sector import create_sector
from api.insetor.repositories.sector import Sectors
from api.utils import serialize_dataclass
import json


class SectorView(View):
    def post(self, request):
        """
        Método Post para criação de um setor
        """
        data = json.loads(request.body)
        sector = create_sector(name=data["name"], code=data["code"])
        serialized_sector = serialize_dataclass(Sectors._make_transport(sector))
        return JsonResponse(
            {"message": "Setor criado com sucesso", "sector": serialized_sector},
            status=201,
        )

    def get(self, request):
        """
        Método Get para retornar todos os setores
        """
        sectors = Sectors.get_all_sectors()
        serialized_sectors = [serialize_dataclass(sector) for sector in sectors]
        return JsonResponse({"sectors": serialized_sectors}, satatus=200)
