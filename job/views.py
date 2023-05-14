from rest_framework import generics, permissions, authentication
from rest_framework.response import Response
from .models import Jobs, Like, ApplyJob
from .serializers import JobSerializer, LikeSerializer, ApplyJobSerializer
from .permissions import IsHR, IsHRorReadOnly, IsCandidateotReadOnly


class JobAPI(generics.ListCreateAPIView):
    permission_classes = [IsHRorReadOnly]
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer


class JobRUDAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsHR]
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer


class ApplyJobAPI(generics.ListCreateAPIView):
    permission_classes = [IsCandidateotReadOnly]
    queryset = ApplyJob.objects.all()
    serializer_class = ApplyJobSerializer


class LikeListCreate(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def create(self, request, *args, **kwargs):
        author_id = self.request.user.id
        jobs_id = self.kwargs.get('jobs_id')
        like = Like.objects.filter(author_id=author_id, jobs_id=jobs_id)
        if like:
            like.delete()
            return Response({'detail': 'Like deleted'})
        object = Like.objects.create(author_id=author_id, jobs_id=jobs_id)
        serializer = LikeSerializer(object)
        return Response(serializer.data)
