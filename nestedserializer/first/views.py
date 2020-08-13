from .models import Hospital, Doctor
from .serializers import HospitalSerializer, DoctorSerializer
from rest_framework import  status
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from rest_framework.authentication import TokenAuthentication
# class HospitalAPIView(ModelViewSet):
#     queryset = Hospital.objects.all()
#     serializer_class = HospitalSerializer
#
#
# class DoctorAPIView(ModelViewSet):
#     queryset = Doctor.objects.all()
#     serializer_class = DoctorSerializer

class HospitalApiView(APIView):
    def get(self,request, pk=None):
        if pk:
            try:
                hospital = Hospital.objects.get(pk=pk)
                serialize = HospitalSerializer(hospital)
            except Hospital.DoesNotExist:
                return Response('object dose not exist', status=status.HTTP_204_NO_CONTENT)
        else:
            hospital = Hospital.objects.all()
            serialize = HospitalSerializer(hospital, many=True)
        return Response(serialize.data)

    def post(self,request):
        data = request.data
        serialize = HospitalSerializer(data=data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response('invalid json data', status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        data = request.data
        hospital = Hospital.objects.get(pk=pk)
        serialize = HospitalSerializer(data=data, instance=hospital)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response('Invalid json Dat Not possible to update', status=status.HTTP_201_CREATED)

    def delete(self,request,pk):
        hospital = Hospital.objects.get(pk=pk)
        hospital.delete()
        return Response('record deleted successfully',status=status.HTTP_200_OK)


class DoctorApiView(APIView):
    def get(self,request, pk=None):
        if pk:
            try:
                hospital = Doctor.objects.get(pk=pk)
                serialize = DoctorSerializer(hospital)
            except Doctor.DoesNotExist:
                return Response('object dose not exist', status=status.HTTP_204_NO_CONTENT)
        else:
            hospital = Doctor.objects.all()
            serialize = DoctorSerializer(hospital, many=True)
        return Response(serialize.data)

    def post(self,request):
        data = request.data
        serialize = DoctorSerializer(data=data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response('invalid json data', status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        data = request.data
        hospital = Doctor.objects.get(pk=pk)
        serialize = DoctorSerializer(data=data, instance=hospital)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response('Invalid json Dat Not possible to update', status=status.HTTP_201_CREATED)

    def delete(self,request,pk):
        hospital = Doctor.objects.get(pk=pk)
        hospital.delete()
        return Response('record deleted successfully',status=status.HTTP_200_OK)
