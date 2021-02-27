from django.contrib.auth import get_user_model
from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Tag, Todo, TodoList, TodoListSerializer

User = get_user_model()


class AboutTodoList(ListCreateAPIView):
    authentication_classes = [JWTAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TodoListSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return TodoList.objects.all()
        return TodoList.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
