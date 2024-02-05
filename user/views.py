from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserLoginSerializer, UserRegisterSerializer
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView





class UserRegisterAPi(APIView):
    """

    User modeli uchun post() funksiyasi , bu funksiya yordamida request qabul qilinadi va UserRegisterSerializer 
    orqali validatsiya qilamiz va saqlaymiz 
    Oxirida saqlangan datani Response da qaytaramiz!

    """
    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    


class UserLoginAPi(CreateAPIView):
    serializer_class = UserLoginSerializer

  
