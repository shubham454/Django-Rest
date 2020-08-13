from django.shortcuts import render,HttpResponse
from first.models import Student
from django.core.serializers import serialize
from first.mixins import SerializeMixin,HttpResponseMixin
from django.views.generic import View
import json
from first.forms import StudentForm
from first.utils import is_json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class CrudCBV(SerializeMixin,HttpResponseMixin,View):
    def get_obj_by_id(self,id,*args,**kwargs):
        try:
            stu = Student.objects.get(id=id)
        except Student.DoesNotExist:
            stu = None
        return stu
    def get(self,request,id,*args,**kwargs):
        stu = self.get_obj_by_id(id=id)
        print(stu,'*****************************')
        if stu is None:
            json_data = json.dumps({'msg':'no match data exist'})
            return self.render_to_http_response(json_data)
        json_data = self.serialize([stu,])
        return self.render_to_http_response(json_data)
    def put(self,request,id,*args,**kwargs):
        stu = self.get_obj_by_id(id=id)
        if stu is None:
            json_data = json.dumps({'msg':'no match data exist for update'})
            return self.render_to_http_response(json_data,status_code=400)
        data = request.body
        if not is_json(data):
            json_data = json.dumps({'msg':'please provide valid json data only'})
            return self.render_to_http_response(json_data,status_code=400)
        provided_data = json.loads(data)
        original_data = {
        'name':stu.name,
        'rollno':stu.rollno,
        'marks':stu.marks,
        'addr':stu.addr
        }
        original_data.update(provided_data)
        form = StudentForm(original_data,instance=stu)
        if form.is_valid():
            form.save()
            json_data = json.dumps({'msg':'update successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            return self.render_to_http_response(json.dumps(forms.errors),status_code=400)
    def delete(self,request,id,*args,**kwargs):
        stu = self.get_obj_by_id(id = id)
        if stu is None:
            json_data = json.dumps({'msg':'no match data exist'})
            return self.render_to_http_response(json_data)
        stu.delete()
        json_data = json.dumps({'msg':'object delete successfully'})
        return self.render_to_http_response(json_data)

@method_decorator(csrf_exempt,name='dispatch')
class CrudDetailCBV(HttpResponseMixin,SerializeMixin,View):
    def get_obj_by_id(self,id,*args,**kwargs):
        try:
            stu = Student.objects.get(id=id)
        except Student.DoesNotExist:
            stu = None
        return stu
    def get(self,request,*args,**kwargs):
        data = request.body
        if not is_json:
            json_data = {'msg':'please send valid json data'}
            return self.render_to_http_response(json_data,status_code=400)
        data = json.loads(data)
        id = data.get('id',None) # should be in dictonary otherwise not getting data of id
        if id is not None:
            stu = self.get_obj_by_id(id = id)
            if stu is None:
                json_data = json.dumps({'msg':'no match record found'})
                return self.render_to_http_response(json_data,status_code=400)
            json_data = self.serialize([stu,])
            return self.render_to_http_response(json_data)
        qs = Student.objects.all()
        json_data = self.serialize(qs)
        return self.render_to_http_response(json_data)
    def post(self,request,*args,**kwargs):
        data = request.body
        if not is_json(data):
            return self.render_to_http_response(json.dumps({'msg':'please provide valid json data only'}),status_code=400)
        stu_data = json.loads(data)
        form = StudentForm(stu_data)
        if form.is_valid():
            form.save()
            json_data = json.dumps({'msg':'resource created successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_http_response(json_data,status_code=400)
    def delete(self,request,*args,**kwargs):
        data = request.body
        if not is_json:
            json_data = {'msg':'please send valid json data'}
            return self.render_to_http_response(json_data,status_code=400)
        data = json.loads(data)
        id = data.get('id',None) # should be in dictonary otherwise not getting data of id
        if id is not None:
            stu = self.get_obj_by_id(id = id)
            if stu is None:
                json_data = json.dumps({'msg':'no match record found'})
                return self.render_to_http_response(json_data,status_code=400)
            stu.delete()
            json_data = json.dumps({'msg':'delete successfully'})
            return self.render_to_http_response(json_data)
        json_data = json.dumps({'msg':'please provide id for deleting data'})
        return self.render_to_http_response(json_data)
    def put(self,request,*args,**kwargs):
        data = request.body
        if not is_json:
            json_data = {'msg':'please send valid json data'}
            return self.render_to_http_response(json_data,status_code=400)
        data = json.loads(data)
        id = data.get('id',None) # should be in dictonary otherwise not getting data of id
        if id is None:
            json_data = json.dumps({'msg':'please provide id for updating data'})
            return self.render_to_http_response(json_data)
        stu = self.get_obj_by_id(id = id)
        if stu is None:
            json_data = json.dumps({'msg':'no match record found'})
            return self.render_to_http_response(json_data,status_code=400)
        provided_data = data
        original_data = {
        'name':stu.name,
        'rollno':stu.rollno,
        'marks':stu.marks,
        'addr':stu.addr
        }
        original_data.update(provided_data)
        form = StudentForm(original_data,instance=stu)
        if form.is_valid():
            form.save()
            json_data = json.dumps({'msg':'update successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            return self.render_to_http_response(json.dumps(forms.errors),status_code=400)
