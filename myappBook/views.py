# from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from rest_framework.response import Response

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

@api_view(['POST', 'GET'])
def books(request):
    return Response('list of the bookkkks',status = status.HTTP_200_OK)

# class based views:This allow reusable of codes
class BookList(APIView):
    
    def get(self,request):
        author = request.GET.get('author')
        
        if (author):
            return Response({"message":"list of books"},status.HTTP_200_OK)
        
        
        return Response({"message":"list of books"}, status=status.HTTP_200_OK)
    
    def post(self,request):
        return Response({"message":"hello Post"},status=status.HTTP_200_OK)
    
    # django-debug-toolbar
    # pipenv install django-debug-toolbar
    
    # in setting.py add below line
    # INSTALLED_APPS=['debug-toolbar']
    # MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware'],
    # INTERNAL_IPS = ['127.0.0.1']
    
    
    # in views.py add below line
    # path('__debug__/',include('debug_toolbar.urls')),