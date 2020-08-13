from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from django.views.generic import View
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
# @method_decorator(csrf_exempt,name='dispatch')
# class EmployeeCRUDCBV(View):
#     def get(self,request,*args,**kwargs):
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         data=JSONParser().parse(stream)
#         id = data.get('id',None)
#         if id is not None:
#             try:
#                 emp=Employee.objects.get(id=id)
#             except Employee.DoesNotExist:
#                 emp=None
#             if emp is not None:
#                 serializer=EmployeeSerializer(emp)
#                 json_data=JSONRenderer().render(serializer.data)
#                 return HttpResponse(json_data,content_type='application/json')
#             json_data={'msg':'no match record found'}
#             json_data=JSONRenderer().render(json_data)
#             return HttpResponse(json_data,content_type='application/json')
#         qs=Employee.objects.all()
#         serializer=EmployeeSerializer(qs,many=True)
#         json_data=JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data,content_type='application/json')
#     def post(self,request,*args,**kwargs):
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         data=JSONParser().parse(stream)
#         serializer=EmployeeSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             json_data=JSONRenderer().render({'msg':'object created succcessfully'})
#             return HttpResponse(json_data,content_type='application/json')
#         json_data=JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json')
#     def put(self,request,*args,**kwargs):
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         data=JSONParser().parse(stream)
#         id=data.get('id',None)# here condition will be taken as if id is none
#         emp=Employee.objects.get(id=id)
#         serializer=EmployeeSerializer(emp,data=data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             msg={'msg':'Resource updates successfully'}
#             json_data=JSONRenderer().render(msg)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data=JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json')
#     def delete(self,request,*args,**kwargs):
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         data=JSONParser().parse(stream)
#         id=data.get('id',None)
#         emp=Employee.objects.get(id=id)
#         emp.delete()
#         msg={'msg':'Resource delete successfully'}
#         json_data=JSONRenderer().render(msg)
#         return HttpResponse(json_data,content_type='application/json')
from rest_framework.views import APIView
from rest_framework.response import Response
class EmployeeListAPIView(APIView):
    def get(self,request,format=None):
        qs=Employee.objects.all()
        serialize=EmployeeSerializer(qs,many=True)
        return Response(serialize.data)
    def post(self,request,*args):