from django.urls import path
from .views import ContactListCreateAPIView, SubscribeListCreateAPIView


urlpatterns = [
    path('contact/', ContactListCreateAPIView.as_view()),
    path('subscribe/', SubscribeListCreateAPIView.as_view()),
]
