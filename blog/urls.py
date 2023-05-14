from django.urls import path
from . views import BlogListCreateAPIView, BlogRUDAPI, CommentListCreateAPIView


urlpatterns = [
    path('list-create/', BlogListCreateAPIView.as_view()),
    path('rud/<int:pk>/', BlogRUDAPI.as_view()),
    path('<int:blog_id>/comment-list-create/', CommentListCreateAPIView.as_view()),
]
