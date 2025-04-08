from django.contrib import admin
from django.urls import path
from api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('student_api/', views.hello_world),


    # to work with 3rd party application like 'my_app.py'  
    # path('student_api/', views.student_api),

    # to work directly with browseable API such as browser url, (does not need any 3rd party application like 'my_app.py')
    path('student_api/', views.student_api),
    path('student_api/<int:pk>', views.student_api),
]


