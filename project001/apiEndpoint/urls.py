
from django.urls import path, include
from .views import  GetInfoView

urlpatterns = [
    path('', GetInfoView.as_view(), name="get_info")
]
