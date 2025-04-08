from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status

# Create your views here.
# @api_view()
# def hello_world(request):
#     return Response({'msg': 'Hello World'})

# @api_view(['GET'])
# def hello_world(request):
#     return Response({'msg': 'Hello World'})

# @api_view(['POST'])
# def hello_world(request):
#     if request.method == "POST":
#         print(request.data)
#         return Response({'msg': 'This is POST request'})

# @api_view(['GET', 'POST'])
# def hello_world(request):
#     if request.method == "GET":
#         return Response({'msg': 'Hello World'})
    
#     if request.method == "POST":
#         print(request.data)
#         return Response({'msg': 'This is POST request' , 'data': request.data})
    




# # function based API View   
# # to work with 3rd party application like 'my_app.py'   

# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def student_api(request):
#     id = request.data.get('id')

#     if request.method == "GET":
#         if id is not None:
#             student = Student.objects.get(id = id)
#             serializer = StudentSerializer(student)
#             return Response(serializer.data)
#         else:
#             students = Student.objects.all()
#             serializer = StudentSerializer(students, many = True)
#             return Response(serializer.data)



#     if request.method == 'POST':
#         serializer = StudentSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save() 
#             return Response({'msg': 'Data Created'})
        
#         return Response(serializer.errors)



#     if request.method == 'PUT':
#         student = Student.objects.get(id = id)
#         serializer = StudentSerializer(student, data = request.data, partial = True)

#         if serializer.is_valid():
#             serializer.save() 
#             return Response({'msg': 'Data Updated'})
        
#         return Response(serializer.errors)



#     if request.method == 'DELETE':
#         student = Student.objects.get(id = id)

#         student.delete()
#         return Response({'msg': 'Data Deleted'})
    



# function based API View   
# to work directly with browseable API such as browser url, (does not need any 3rd party application like 'my_app.py')

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def student_api(request, pk = None):
    id = pk

    if request.method == "GET":
        if id is not None:
            student = Student.objects.get(id = id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        else:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many = True)
            return Response(serializer.data)



    if request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response({'msg': 'Data Created'}, status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



    if request.method == 'PUT':
        student = Student.objects.get(id = id)
        serializer = StudentSerializer(student, data = request.data)

        if serializer.is_valid():
            serializer.save() 
            return Response({'msg': 'Complete Data Updated'})
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    


    if request.method == 'PATCH':
        student = Student.objects.get(id = id)
        serializer = StudentSerializer(student, data = request.data, partial = True)

        if serializer.is_valid():
            serializer.save() 
            return Response({'msg': 'Partial Data Updated'})
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



    if request.method == 'DELETE':
        student = Student.objects.get(id = id)

        student.delete()
        return Response({'msg': 'Data Deleted'})
    
