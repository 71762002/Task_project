from rest_framework import serializers
from .models import User
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token



class UserRegisterSerializer(serializers.ModelSerializer):
    reply_password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ("id", "email", "first_name", "last_name", "password", "reply_password")

        extra_kwargs = {"password" : {"write_only" : True}}


        """
        UserRegisterSerializer classimiz registratsiyadan kelgan malumotlarni birinchi validatsiya qilib keyin create (yaratib) beradi
        """


    def validate(self, attrs):
        attrs = super().validate(attrs)
        email = attrs['email']
        user = self.Meta.model.objects.filter(email=email).first()
        if user:
            raise serializers.ValidationError("Bunday foydalanuvchi mavjud!")
        password = attrs["password"]
        reply_password = attrs.pop("reply_password")
        if password != reply_password:
            raise serializers.ValidationError("Passwordlar mos kelmadi!")
        return attrs
    

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        if not password or not email:
            return Response({
                "error" : "Email yoki password xato!"
            },status=HTTP_400_BAD_REQUEST)
        data = {"email" : email, "password" : password}
        user = authenticate(**data)
        if not user:
            return Response({
                "error" : "Bunday foydalanuvchi mavjud emas!"
            })
        return attrs
    

    
    def to_representation(self, instance):
        token, _ = Token.objects.get_or_create(user__email=instance['email'])
        return {'token': token.key}
    


    def create(self, validated_data):
        return validated_data
 
       

