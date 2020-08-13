from rest_framework.serializers import ModelSerializer
from .models import Hospital, Doctor


class DoctorSerializer(ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class HospitalSerializer(ModelSerializer):
    doctor = DoctorSerializer(many=True)

    class Meta:
        model = Hospital
        fields = '__all__'
