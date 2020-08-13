from django.shortcuts import HttpResponse
import json
from django.core.serializers import serialize
class HttpResponseMixin:
    def render_to_http_response(self,json_data,status=200):
        return HttpResponse(json_data,content_type = 'application/json')

class SerializeMixin:
    def serialize(self,qs):
        json_data = serialize('json',qs)
        p_data = json.loads(json_data)
        flist = []
        for obj in p_data:
            flist.append(obj['fields'])
        json_data = json.dumps(flist)
        return json_data
