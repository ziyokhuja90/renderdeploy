from django.shortcuts import render

from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def home(request):
    db = Product.objects.all()
    serializer = ProductSerializer(db , many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"created"} , status=201)
    else:
        return Response({"message":"error"})