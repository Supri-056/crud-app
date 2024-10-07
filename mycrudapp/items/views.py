from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import item
from . serializers import itemSerializer

# List all items or create a new item
class ItemListCreate(generics.ListCreateAPIView):
    queryset = item.objects.all()
    serializer_class = itemSerializer

# Retrieve, update or delete an item by ID
class ItemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = item.objects.all()
    serializer_class = itemSerializer
