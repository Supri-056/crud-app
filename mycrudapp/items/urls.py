from django.urls import path
from .views import ItemListCreate, ItemRetrieveUpdateDestroy

urlpatterns = [
    path('items/', ItemListCreate.as_view(), name='item-list-create'),
    path('items/<int:pk>/', ItemRetrieveUpdateDestroy.as_view(), name='item-retrieve-update-destroy'),
]
# Include the items app URLs in the project's mycrudapp/urls.py:
# python

