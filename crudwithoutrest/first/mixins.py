from django.core.serializers import serialize
from django.shortcuts import HttpResponse
import json

class SerializeMixin(object):
    def serialize(self,qs):
        json_data = serialize('json',qs)
        p_data = json.loads(json_data)
        flist =[]
        for obj in p_data:
            flist.append(obj.get("fields"))
        json_data = json.dumps(flist)
        return json_data

class HttpResponseMixin:
    def render_to_http_response(self,json_data,status_code = 200):
        return HttpResponse(json_data,content_type = 'application/json')
