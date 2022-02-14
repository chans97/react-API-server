from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import GameUser
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = GameUser.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()


class UserByLevelView(generics.ListAPIView):
    serializer_class = UserSerializer
    
    def get_queryset(self):
        return GameUser.objects.filter(level=self.kwargs['level'])