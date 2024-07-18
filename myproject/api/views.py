
from django.shortcuts import render
from rest_framework import generics

from rest_framework.response import Response

from rest_framework import status

from .serializers import BookSerializer

from rest_framework.views import APIView

from .models import Book


class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def delete(self, request,*args, **kwargs):
        Book.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'



class BookList(APIView):
    def get(self, request, format =None):
        title = request.GET.get('title','')

        if title:
            books = Book.objects.filter(title__icontains=title)
        else:
            books = Book.objects.all()
        
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


# Create your views here.
