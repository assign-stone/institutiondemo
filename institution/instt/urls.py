from django.urls import path
from . import views
urlpatterns = [
    path("",views.openfactorialform),
    path("calculateFact",views.calculatefactorial),
    path("employeedatashow",views.employeesdata)
]