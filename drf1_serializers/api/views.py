from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

# Create your views here.
# working for serializing process

# Model Object (Single Student Data)
def student_detail(request, pk):
    stud = Student.objects.get(id = pk)
    # print('single object data: ', stud)
    # print()

    serializer = StudentSerializer(stud)
    # print('serializer: ', serializer)
    # print()
    # print('serializer.data: ', serializer.data)
    # print()

    json_data = JSONRenderer().render(serializer.data)
    # print('json_data: ', json_data)

    # return HttpResponse(json_data, content_type='application/json')

    return JsonResponse(serializer.data)


# Query set (All Student Data)
def student_list(request):
    studs = Student.objects.all()
    # print('queryset data: ', studs)
    # print()

    serializer = StudentSerializer(studs, many=True)
    # print('serializer: ', serializer)
    # print()
    # print('serializer.data: ', serializer.data)
    # print()

    json_data = JSONRenderer().render(serializer.data)
    # print('json_data: ', json_data)

    # return HttpResponse(json_data, content_type='application/json')

    return JsonResponse(serializer.data, safe=False)
