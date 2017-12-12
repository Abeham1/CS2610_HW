from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Conversion
from .serializers import ConversionSerializer
from django.shortcuts import get_object_or_404


class  ConversionList(APIView):
    
    def get(self, url):
        conversions = Conversion.objects.all()
        serializer = ConversionSerializer(conversions, many=True)
        return Response(serializer.data)
        
        