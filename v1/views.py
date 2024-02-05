from django.shortcuts import render
from .serializer import Category, LikeDislikeSerializer, Product, LikeDislike
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from .serializer import CategorySerializer, ProductSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateDestroyAPIView,  ListCreateAPIView
from django.db.models import Q



class CategoryAPi(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def get(self, request):
        categorys= Category.objects.order_by("-id").values("id", "title")
        
        return Response({
            "status" : "True",
            "categorys" : categorys
            
        })
    
    
class CategoryDetailAPi(RetrieveUpdateDestroyAPIView):
    """
    lookup_field  bizga "pk" ya'ni malumot ID sini qidirib olib beradi
    """
    lookup_field = 'pk'
    queryset = Category.objects.all()
    serializer_class = CategorySerializer  
    
    


class ProductApi(ListCreateAPIView):
  
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateDelete(RetrieveUpdateDestroyAPIView):
    lookup_field = "id"
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
     
        
class ProductSearch(APIView):
     def get(self, request, *args, **kwargs):
        params = self.request.query_params
        q = params.get("q")
        
        queryset = Product.objects.all()
        
        
        if q:
            queryset = queryset.filter(
                Q(name__icontains=q) | Q(price__icontains=q) |
                Q(description__icontains=q)    
            )
            
        serializer = ProductSerializer(queryset, many=True, context ={"request" : request})
        return Response(serializer.data)
    



class LikeDislikeCreateAPi(ListCreateAPIView):
    queryset = LikeDislike.objects.all()
    serializer_class = LikeDislikeSerializer





