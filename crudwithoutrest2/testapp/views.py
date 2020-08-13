from django.shortcuts import render
from testapp.models import Employee
from testapp.forms import EmployeeForm
from testapp.utils import is_json
from django.views.generic import View
from testapp.mixins import HttpResponseMixin, SerializeMixin
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class EmployeeCRUD(HttpResponseMixin,SerializeMixin,View):
    def get_obj_by_id(self,id):
        try:
            obj = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            obj = None
        return obj
    def get(self,request,*args,**kwargs):
        data = request.body
        if not is_json(data):
            json_data = json.dumps({'msg':'please provide valid json data'})
            return self.render_to_http_response(json_data,status = 400)
        data = json.loads(data)
        id = data.get('id',None)
        if id is not None:
            obj = self.get_obj_by_id(id)
            if obj is None:
                return self.render_to_http_response(json.dumps({'msg':'not match record found'}),status=400)
            json_data = self.serialize([obj,])
            return self.render_to_http_response(json_data)
        obj = Employee.objects.all()
        json_data = self.serialize(obj)
        return self.render_to_http_response(json_data)
    def post(self,request,*args,**kwargs):
        data = request.body
        if not is_json(data):
            json_data = json.dumps({'msg':'please provide valid json data'})
            return self.render_to_http_response(json_data,status=400)
        data = json.loads(data)
        form = EmployeeForm(data)
        if form.is_valid():
            form.save()
            json_data = json.dumps({'msg':'resourse created successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data)
    def put(self,request,*args,**kwargs):
        data = request.body
        if not is_json(data):
            json_data = json.dumps({'msg':'please provide valid json data'})
            return self.render_to_http_response(json_data,status = 400)
        data = json.loads(data)
        id = data.get('id',None)
        if id is not None:
            obj = self.get_obj_by_id(id)
            if obj is None:
                return self.render_to_http_response(json.dumps({'msg':'not match record found'}),status=400)
            provided_data = data
            original_data = {
            'eno':obj.eno,
            'ename':obj.ename,
            'esal':obj.esal,
            'eaddr':obj.eaddr,
            }
            original_data.update(provided_data)
            form = EmployeeForm(original_data,instance=obj)
            if form.is_valid():
                form.save()
                return self.render_to_http_response(json.dumps({'msg':'resoursee update successfully'}))
            if form.errors:
                return self.render_to_http_response(json.dumps(form.errors),status=400)
    def delete(self,request,*args,**kwargs):
        data = request.body
        if not is_json(data):
            json_data = json.dumps({'msg':'please provide valid json data'})
            return self.render_to_http_response(json_data,status = 400)
        data = json.loads(data)
        id = data.get('id',None)
        if id is not None:
            obj = self.get_obj_by_id(id)
            if obj is None:
                return self.render_to_http_response(json.dumps({'msg':'not match record found'}),status=400)
            obj.delete()
            return self.render_to_http_response(json.dumps({'msg':'resoursee delete successfully'}),status=200)
        return self.render_to_http_response(json.dumps({'msg':'please provide id to delete daata'}),status=400)
