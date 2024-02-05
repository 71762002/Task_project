from django.db import models



class DefaultAbstract(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True


class Category(DefaultAbstract):
    title = models.CharField(max_length=100)



class Product(DefaultAbstract):
    name = models.CharField(max_length=100)
    price = models.IntegerField(verbose_name=100)
    description = models.TextField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to="media/image")
   

    def __str__(self) -> str:
        return self.name
    


class  LikeDislike(DefaultAbstract):
    like_dislike = models.BooleanField(default = None, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)


    def __str__(self) -> str:
        return f"{self.id} - {self.like_dislike}"

    
        
