from django.shortcuts import render
from basicapi.models import Book
from django.http import JsonResponse
from basicapi.serializer import BookSerilaizer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView


# Create your views here.
'''
@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerilaizer(books, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def book_create(request):
    serializer = BookSerilaizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_206_PARTIAL_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def books(request, pk):
    try:


        book = Book.objects.get(pk=pk)
    except:
        return Response({
            'error' : 'Book doesnt exist'
        }, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        
        serializer = BookSerilaizer(book)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = BookSerilaizer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''

class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerilaizer(books, many=True)
        return Response(serializer.data)

class BookCreate(APIView):
    def post(self, request):
        serializer = BookSerilaizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_206_PARTIAL_CONTENT)

class BookDetail(APIView):
    def get_book_by_pk(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except:
            return Response({
            'error' : 'Book doesnt exist'
            }, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        book = self.get_book_by_pk(pk)
        serializer = BookSerilaizer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = self.get_book_by_pk(pk)
        serializer = BookSerilaizer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = self.get_book_by_pk(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






