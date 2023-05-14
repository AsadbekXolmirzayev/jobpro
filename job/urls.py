from django.urls import path
from .views import JobAPI, LikeListCreate, ApplyJobAPI, JobRUDAPI


urlpatterns = [
    path('list-create/', JobAPI.as_view()),
    path('rud/<int:pk>/', JobRUDAPI.as_view()),
    path('apply-job/', ApplyJobAPI.as_view()),
    path('like/<int:jobs_id>/', LikeListCreate.as_view()),
]
