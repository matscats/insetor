from django.views import View
from django.http.response import JsonResponse
from api.insetor.services.employee import create_employee
from api.insetor.repositories.employee import Employees
from api.utils import serialize_dataclass
import json


class EmployeeView(View):
    def post(self, request):
        """
        Método Post para a criação de um funcionário
        """
        data = json.loads(request.body)
        employee = create_employee(name=data["name"], sector=data["sector"])
        serialized_employee = serialize_dataclass(Employees._make_transport(employee))
        return JsonResponse(
            {
                "message": "Funcionário criado com sucesso",
                "employee": serialized_employee,
            },
            status=201,
        )

    def get(self, request, sector_id):
        """
        Vamos retornar todos os funcionários que trabalham em um setor
        """
        employees = Employees.get_all_employees_from_sector(sector_id=sector_id)
        serialized_employees = [serialize_dataclass(employee) for employee in employees]
        return JsonResponse({"employees": serialized_employees}, status=200)
