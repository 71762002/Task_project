from rest_framework import serializers
from .models import Category, Product, LikeDislike


class CategorySerializer(serializers.ModelSerializer):


    class Meta:
        model = Category
        fields = ("id", "title")

    


class ProductSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Product
        fields = ("id", "name", "price", "description", "image", "category")
        extra_kwargs = {"category" : {"required" : True}}


class LikeDislikeSerializer(serializers.ModelSerializer):
    like_dislike = serializers.IntegerField()

    class Meta:
        model = LikeDislike
        fields = ("id", "like_dislike", "product")


        """
        LikeDislikeSerializerda create funksiyasini chaqiramiz productga like_dislike create qilamiz 
        bunda validated_datadan malumot qabul qilib ya'ni olib LikeDislike madelimizga get_or_create qilamiz
          get_or_createdan sababi avval bu praductga like yoki dislike bosgan bulishi ham mumkin
        """


    def create(self, validated_data):
        product = validated_data.get("product")
        like_dislike = validated_data.get("like_dislike")
        ld, _ = LikeDislike.objects.get_or_create(user_id = self.context['request'].user.id, product_id=product.id)
        
        if like_dislike == 1 and ld.like_dislike != True:
            ld.like_dislike = True
            ld.save()
        elif like_dislike == 2 and ld.like_dislike != False:
            ld.like_dislike = False
            ld.save()
        elif like_dislike == 3 and ld.like_dislike != None:
            ld.like_dislike = None
            ld.save()
        
        return ld
    
    def to_representation(self, instance):
        res = super().to_representation(instance)
        res['like_dislike'] = instance.like_dislike
        return res
    
    """
    to_representation ni ishlatishimizdan maqsad like_dislike qiymatlari bazaviy ya'ni 0 va 1 bulib qaytayotganligi uchun
    bu funksiya bilan True False qiymatlarini qaytarib qo'ydik 
    """

    





