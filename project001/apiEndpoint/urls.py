
from django.urls import path, include
from .views import  GetInfoView

urlpatterns = [
    path('get_slack_info/', GetInfoView.as_view(), name="get_info")
]
