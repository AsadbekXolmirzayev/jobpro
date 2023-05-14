from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.AccountRegisterView.as_view()),
    path('login/', views.LoginView.as_view()),

    path('retrieve-update/<int:pk>/', views.AccountRetrieveUpdateView.as_view()),
    path('my-account/', views.MyAccountAPIView.as_view()),

]
