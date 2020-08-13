from django.shortcuts import render
# from testapp.serializers import NameSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
# Create your views here.
# class TestViewSet(ViewSet): # this is plane viewset class
#     def list(self,request):
#         colors=['RED','GREEN','YELLOW','ORANGE']
#         return Response({'msg':'Wish you colorful life in 2020','color':colors})
#     def create(self,request):
#         serializer=NameSerializer(data=request.data)
#         if serializer.is_valid():
#             name=serializer.data.get('name')
#             msg=('Hello {} Your Life will be settle in 2020'.format(name))
#             return Response({'msg':msg})
#         return Response(serializer.errors,status=400)
#     def retrive(self,request,pk=None):
#         return Response({'msg':'Response is from retrive method'})
#     def update(self,request,pk=None):
#         return Response({'msg':'Response is from update method'})
#     def partial_update(self,request,pk=None):
#         return Response({'msg':'Response is from partial_update method'})
#     def destroy(self,request,pk=None):
#         return Response({'msg':'Response is from destroy method'})

# now we use modelviewset
from testapp.models import Employee
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from testapp.permissions import IsReadOnly,IsGetOrPatch,SunnyPermission
from testapp.serializers import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet
class TestViewSet(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    #here i anabled authentication locally
    authentication_classes=[TokenAuthentication]
    permission_classes=[SunnyPermission]
