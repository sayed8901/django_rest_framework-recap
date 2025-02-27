from django.shortcuts import render
import io
from .models import Student
from .serializers import StudentSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.utils.decorators import method_decorator
from django.views import View


# class based views

@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):

    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)

        id = python_data.get('id', None)

        if id is not None:
            stud = Student.objects.get(id=id)
            serializer = StudentSerializer(stud)

            return JsonResponse(serializer.data, safe=False)
        
        all_studs = Student.objects.all()
        serializer = StudentSerializer(all_studs, many=True)

        return JsonResponse(serializer.data, safe=False)



    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)

        serializer = StudentSerializer(data = python_data)

        if serializer.is_valid():
            serializer.save()

            response = {'msg': 'Data Inserted'}
            # json_data = JSONRenderer().render(response)
            # return HttpResponse(json_data, content_type='application/json')
        
            # alternatively we can also use 'JsonResponse' instead of 'JSONRenderer' & 'HttpResponse'...
            return JsonResponse(response, safe=False)

        # json_data = JSONRenderer().render(serializer.errors)
        # return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(serializer.errors, safe=False)



    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)

        id = python_data.get('id')

        stud = Student.objects.get(id = id)

        # creating a serializer data to handle & update student data

        # Complete Update --> it required all data from frontend / clent
        # serializer = StudentSerializer(stud, data = python_data)

        # Partial Update --> All data fields are not required
        serializer = StudentSerializer(stud, data = python_data, partial=True)

        if serializer.is_valid():
            serializer.save()

            response = {'msg': 'Data Updated'}
            # json_data = JSONRenderer().render(response)
            # return HttpResponse(json_data, content_type='application/json')
        
            # alternatively we can also use 'JsonResponse' instead of 'JSONRenderer' & 'HttpResponse'...
            return JsonResponse(response, safe=False)

        # json_data = JSONRenderer().render(serializer.errors)
        # return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(serializer.errors, safe=False)



    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)

        id = python_data.get('id')

        stud = Student.objects.get(id = id)

        # deleting student object data
        stud.delete()

        # creating a serializer data to handle & delete student data
        serializer = StudentSerializer(stud, data = python_data, partial=True)
        
        response = {'msg': 'Data Deleted Succefully'}
        # json_data = JSONRenderer().render(response)
        # return HttpResponse(json_data, content_type='application/json')
        
        # alternatively we can also use 'JsonResponse' instead of 'JSONRenderer' & 'HttpResponse'...
        return JsonResponse(response, safe=False)




