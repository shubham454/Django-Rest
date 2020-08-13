from django.shortcuts import render
from testapp.serializers import EmployeeSerializer
from testapp.models import Employee
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import (ListAPIView,CreateAPIView,DestroyAPIView,
RetrieveAPIView,UpdateAPIView,ListCreateAPIView,RetrieveUpdateAPIView,
RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView)
# Create your views here.
# class EmployeeCRUDAPIView(APIView):
#     def get(self,request,format=None):
#         qs=Employee.objects.all()
#         serializer=EmployeeSerializer(qs,many=True)
#         return Response(serializer.data)

# Now we are using APIView generic class
class EmployeeListAPIView(ListAPIView):
    queryset=Employee.objects.all() # to fetch all data
    serializer_class=EmployeeSerializer
    def get_queryset(self):
        qs=Employee.objects.all()#to get data by serching
        name=self.request.GET.get('ename')
        if name is not None:
            qs=qs.filter(ename__icontains=name)
        return qs
class EmployeeCreateAPIView(CreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
class EmployeeUpdateAPIView(UpdateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field='id'
class EmployeeDestroyAPIView(DestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field='id'

# we have to provide this all f=crud functinality by using only two end points
class EmployeeListCreateAPIView(ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    def get_queryset(self):
        qs=Employee.objects.all()#to get data by serching
        name=self.request.GET.get('ename')
        if name is not None:
            qs=qs.filter(ename__icontains=name)
        return qs
class EmployeeRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field='id'
class EmployeeRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field='id'
class EmployeeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field='id'
