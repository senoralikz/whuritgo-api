import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.expense import Expense
from ..serializers import ExpenseSerializer, UserSerializer

# Create your views here.
class Expenses(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = ExpenseSerializer
    def get(self, request):
        """Index request"""
        expense = Expense.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = ExpenseSerializer(expense, many=True).data
        return Response({ 'expenses': data })

    def post(self, request):
        """Create request"""
        data = json.loads(request.body)
        # Add user to request data object
        data['expense']['owner'] = request.user.id
        expense = ExpenseSerializer(data=data['expense'])
        if expense.is_valid():
            expense.save()
            return Response({ 'expense': expense.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(expense.errors, status=status.HTTP_400_BAD_REQUEST)

class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        expense = get_object_or_404(Expense, pk=pk)
        if not request.user.id == expense.owner.id:
            raise PermissionDenied('Unauthorized, you do not have this expense')

        # Run the data through the serializer so it's formatted
        data = ExpenseSerializer(expense).data
        return Response({ 'expense': data })

    def delete(self, request, pk):
        """Delete request"""
        expense = get_object_or_404(Expense, pk=pk)
        if not request.user.id == expense.owner.id:
            raise PermissionDenied('Unauthorized, you do not have this expense')
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        data = json.loads(request.body)
        # Remove owner from request object
        if data['expense'].get('owner', False):
            del data['expense']['owner']

        expense = get_object_or_404(Expense, pk=pk)
        # Check if user is the same as the request.user.id
        if not request.user.id == expense.owner.id:
            raise PermissionDenied('Unauthorized, you do not have this expense')

        # Add owner to data object now that we know this user owns the resource
        data['expense']['owner'] = request.user.id
        # Validate updates with serializer
        data = ExpenseSerializer(expense, data=data['expense'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
