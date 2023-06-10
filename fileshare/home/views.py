from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response

from .serializers import FileListSerializer
# Create your views here.

class HandleFileUpload(APIView):

    def get(self, request):
        return Response({'status':200,'message':"Success"})

    def post(self, request):
        try:
            data = request.data
            print("Data",data)
            serializer = FileListSerializer(data=data)
            
            if serializer.is_valid():
                
                serializerResponse = serializer.save()
                
                return Response({'status':200,'message':"Filed Uploaded Successfully","data":serializerResponse})
            else:
                return Response({'status':400,'message':"Something wrong",'data': serializer.errors})
                                

        except Exception as e:
            return Response({'status':400,'message':"Wrong Information",'data': e})
