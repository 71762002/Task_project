from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserRegisterSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token



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
    

class UserLoginAPi(APIView):

    """
    UserLoginAPi classda post() funksiyamiz request qabul qilib ya'ni registratsiyadan o'tgan ma'lumotlarni tekshiradi va login qilib token qaytaradi
    """
    def post(self, request):
        data = request.data
        email = data.get("email")
        password = data.get("password")
        if not password or not email:
            return Response({
                "error" : "Email yoki password mavjud emas!"
            },status=HTTP_400_BAD_REQUEST)
        
        data = {"email" : email, "password" : password}
        user = authenticate(request, **data)
        if not user:
            return Response({
                "error" : "Bunday foydalanuvchi yo'q!"
            })
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            "token" : token.key
        })