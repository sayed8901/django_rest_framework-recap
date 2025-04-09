from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status

from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets



# It will provide List and Retrieve only, doesn't provide Create, Update and Delete method
# class StudentViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer



# It will provide List, Retrieve, Create, Update and Delete all these methods
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    

# class StudentViewSet(viewsets.ViewSet):
#     def list(self, request):
#         # print("=========== inside List =========")
#         # print("Basename: ", self.basename)
#         # print("Action: ", self.action)
#         # print("Detail: ", self.detail)
#         # print("Suffix: ", self.suffix)
#         # print("Name: ", self.name)
#         # print("Description: ", self.description)

#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)
    

#     def retrieve(self, request, pk = None):
#         id = pk
        
#         if id is not None:
#             student = Student.objects.get(id = id)
#             serializer = StudentSerializer(student)
#             return Response(serializer.data)
        
    
#     def create(self, request):
#         serializer = StudentSerializer(data = request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Data Created'}, status = status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
#     def update(self, request, pk):
#         id = pk
        
#         student = Student.objects.get(id = id)
#         serializer = StudentSerializer(student, data = request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Complete Data Updated'})
        
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

#     def partial_update(self, request, pk):
#         id = pk
        
#         student = Student.objects.get(id = id)
#         serializer = StudentSerializer(student, data = request.data, partial = True)

#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Partial Data Updated'})
        
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

#     def destroy(self, request, pk):
#         id = pk
        
#         student = Student.objects.get(id = id)
#         student.delete()
#         return Response({'msg': 'Data Deleted'})
