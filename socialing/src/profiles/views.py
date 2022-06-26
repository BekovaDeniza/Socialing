from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView

from .models import UserNet
from .serializers import GetUserNetSerializer


class GetUserNetView(RetrieveAPIView):
    """Вывод профиля пользователя
    """
    queryset = UserNet.objects.all()
    serializer_class = GetUserNetSerializer

