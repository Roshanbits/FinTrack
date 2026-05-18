from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Transaction
from .serializers import TransactionSerializer
from .services import classify_transaction

# Create your views here.
@api_view(['POST'])
def create_transaction(request):
    customer_name= request.data.get('customer_name')
    transaction_type = request.data.get('transaction_type')
    amount = request.data.get('amount')
    
    #Business Logic
    category = classify_transaction(transaction_type)
    
    #Save Data
    transaction = Transaction.objects.create(
        customer_name = customer_name,
        transaction_type = transaction_type,
        amount = amount,
        category = category
    )
    
    serializer = TransactionSerializer(transaction)
    return Response(serializer.data)
    
@api_view(['GET'])
def get_transactions(request):
    transactions=Transaction.objects.all()
    serializers = TransactionSerializer(transactions, many=True)
    return Response(serializers.data)
