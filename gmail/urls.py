from django.urls import path
from .views import *

urlpatterns = [
    path('send-email/', ConsultViewSet.as_view()),
]


