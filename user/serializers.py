from rest_framework import serializers
from .models import User



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