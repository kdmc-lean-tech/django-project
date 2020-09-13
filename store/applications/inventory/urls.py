from django.urls import path
from .views import getVendors

urlpatterns = [
    path('vendors', getVendors)
]
