from rest_framework import generics, permissions
from .models import Blog, Comment
from .serializers import BlogListCreateSerializer, BlogRUDSerializer, CommentSerializer
from .permissions import IsAdminOrReadOnly, IsAdmin, IsOwnUserOrReadOnly


class BlogListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Blog.objects.all()
    serializer_class = BlogListCreateSerializer


class BlogRUDAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdmin]
    queryset = Blog.objects.all()
    serializer_class = BlogRUDSerializer


class CommentListCreateAPIView(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/blog/api/{post_id}/comment-list-create/
    queryset = Comment.objects.filter(parent_comment__isnull=True)
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['blog_id'] = self.kwargs.get('blog_id')
        return ctx

    def get_queryset(self):
        qs = super().get_queryset()
        blog_id = self.kwargs.get('blog_id')
        qs = qs.filter(blog_id=blog_id)
        return qs

