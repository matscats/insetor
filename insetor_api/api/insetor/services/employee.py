from api.insetor.models.employee import Employee
from api.insetor.models.sector import Sector


def create_employee(name: str, sector: Sector) -> Employee:
    employee = Employee.objects.create(name=name, sector=sector)
    return employee
