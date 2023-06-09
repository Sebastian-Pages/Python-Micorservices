# from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, User
from .producer import publish
from .serializers import ProductSerializer
import random

# Create your views here.
class ProductViewSet(viewsets.ViewSet):

    # /api/products
    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products,many = True)
        return Response(serializer.data)
    
    # /api/products
    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_created', serializer.data)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    # /api/products/<str:id>
    def retrieve(self, request,pk=None):
        products = Product.objects.get(id=pk)
        serializer = ProductSerializer(products)
        return Response(serializer.data)

    def update(self, request,pk=None):
        products = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=products,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_updated',serializer.data)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

    def destroy(self, request,pk=None):
        products = Product.objects.get(id=pk)
        products.delete()
        publish('product_deleted',pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id':user.id
        })