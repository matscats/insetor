from api.insetor.models.employee import Employee
from api.insetor.transports.employee import EmployeeTransport
from api.insetor.repositories.sector import Sectors
import uuid
import typing
from django.shortcuts import get_object_or_404


class Employees:
    @staticmethod
    def _make_transport(obj: Employee) -> EmployeeTransport:
        return EmployeeTransport(
            id=obj.id, name=obj.name, sector=Sectors._make_transport(obj.sector)
        )

    @staticmethod
    def get_employee(employee_id: uuid.UUID) -> EmployeeTransport:
        employee = get_object_or_404(Employee, id=employee_id)
        return Employees._make_transport(employee)

    @staticmethod
    def get_all_employees() -> typing.Sequence[EmployeeTransport]:
        employees = Employees.objects.all()
        return [Employees._make_transport(employee) for employee in employees]

    @staticmethod
    def get_all_employees_from_sector(
        sector_id: uuid.UUID,
    ) -> typing.Sequence[EmployeeTransport]:
        employees = Employee.objects.select_related("sector").filter(sector=sector_id)
        return [Employees._make_transport(employee) for employee in employees]
