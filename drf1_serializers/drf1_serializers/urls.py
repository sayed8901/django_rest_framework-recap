from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stud_info/<int:pk>', views.student_detail),
    path('stud_info/', views.student_list),
]
