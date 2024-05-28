from api.insetor.models.employee import Employee
from api.insetor.models.sector import Sector
from django.shortcuts import get_object_or_404
import uuid


def create_employee(name: str, sector_id: uuid.UUID) -> Employee:
    sector = get_object_or_404(Sector, id=sector_id)
    employee = Employee.objects.create(name=name, sector=sector)
    return employee
