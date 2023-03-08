from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth.models import User

from .serializer import RegisterSerializer

# class UserView(mixins.CreateModelMixin, generics.GenericAPIView):
# class UserView(generics.CreateAPIView):
#     """
#
#     """
    # def post(self, request, *args, **kwargs):
    #     # return super().create(request, *args, **kwargs)
    #     return self.create(request, *args, **kwargs)


class UserView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """

    """
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class UsernameIsExistedView(APIView):

    def get(self, request, username):
        count = User.objects.filter(username=username).count()
        return Response({'username': username, 'count': count})


class EmailIsExistedView(APIView):

    def get(self, request, email):
        count = User.objects.filter(email=email).count()
        return Response({'email': email, 'count': count})
