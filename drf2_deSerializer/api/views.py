from django.shortcuts import render
import io
from .serializers import StudentSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)

        serializer = StudentSerializer(data=python_data)

        if serializer.is_valid():
            serializer.save()
            response = {'msg': 'Data Created'}
            # json_data = JSONRenderer().render(response)
            # return HttpResponse(json_data, content_type='application/json')
        
            # alternatively we can also use 'JsonResponse' instead of 'JSONRenderer' & 'HttpResponse'...
            return JsonResponse(response, safe=False)

        # json_data = JSONRenderer().render(serializer.errors)
        # return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(serializer.errors, safe=False)
