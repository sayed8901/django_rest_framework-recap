from django.shortcuts import get_object_or_404
from .models import Student
from .serializers import StudentSerializer
from rest_framework import generics


class StudentListCreateView(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class StudentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer

    def get_object(self):
        student = get_object_or_404(Student, id = self.kwargs["pk"])
        return student


