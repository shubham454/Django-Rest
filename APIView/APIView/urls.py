"""APIView URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testapp import views
from rest_framework.authtoken import views as v1

urlpatterns = [
    path('get-api-token',v1.obtain_auth_token,name='get-api-token'),
    path('admin/', admin.site.urls),
    # path('api/',views.EmployeeCRUDAPIView.as_view()),
    # path('api/',views.EmployeeListAPIView.as_view()),
    # path('api/',views.EmployeeCreateAPIView.as_view()),
    path('api/',views.EmployeeListCreateAPIView.as_view()),
    # path('api/<int:id>/',views.EmployeeRetrieveAPIView.as_view()),
    # path('api/<int:id>/',views.EmployeeUpdateAPIView.as_view()),
    # path('api/<int:id>/',views.EmployeeDestroyAPIView.as_view()),
    # path('api/<int:id>/',views.EmployeeRetrieveUpdateAPIView.as_view()),
    # path('api/<int:id>/',views.EmployeeRetrieveDestroyAPIView.as_view()),
    path('api/<int:id>/',views.EmployeeRetrieveUpdateDestroyAPIView.as_view()),


]
