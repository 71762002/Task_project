"""
signal yozishimizdan maqsad Foydalanuvchi login qilayotgan vaqti baravariga ya'ni hu bilan birgalikda Token ham create bulish kerak
shunda signal ishga tushadi  

User create va Token create
"""





from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models  import Token

from .models import User

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
   
    if created:
        Token.objects.create(user=instance)



