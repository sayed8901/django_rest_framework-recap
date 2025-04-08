from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('student_api/', views.StudentListCreateView.as_view()),
    path('student_api/<int:pk>', views.StudentRetrieveUpdateDestroyView.as_view()),
]