from django.urls import path
from .views import (
    CategoryDetailAPi,
    CategoryAPi,
    ProductApi,
    ProductUpdateDelete,
    ProductSearch,
    LikeDislikeCreateAPi
    
    
    )

urlpatterns = [
    path("category/<int:pk>/", CategoryDetailAPi.as_view()),
    path("category/create/", CategoryAPi.as_view()),
    path("product/create/", ProductApi.as_view()),
    path("product/<int:id>/", ProductUpdateDelete.as_view()),
    path("product/search/", ProductSearch.as_view()),
    path("product/like_dislike/", LikeDislikeCreateAPi.as_view())

    
]