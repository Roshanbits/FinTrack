from django.urls import path
from .views import create_transaction,get_transactions

urlpatterns = [
    path('create/',create_transaction),
    path('all/',get_transactions),
]
