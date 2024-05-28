from django.urls import path
from api.insetor.views.employee import EmployeeView
from api.insetor.views.sector import SectorView

urlpatterns = [
    path("sector/", SectorView.as_view()),
    path("employee/", EmployeeView.as_view()),
    path("employee/<uuid:sector_id>/", EmployeeView.as_view()),
]
