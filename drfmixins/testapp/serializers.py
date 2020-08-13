from rest_framework import serializers
from testapp.models import Employee

def multiple_of_1000(value):
    if value%1000!=0:
        raise serializers.ValidationError('employee salary shuld be in multiple of 1000')

class EmployeeSerializer(serializers.ModelSerializer):
    esal=serializers.FloatField(validators=[multiple_of_1000])
    class Meta:
        model=Employee
        fields="__all__"
    def validate_esal(self,value):
        if value<5000:
            raise serializers.ValidationError('employee salary should be more than 5000')
        return value
    def validate(self,data):
        eno=data.get('eno')
        esal=data.get('esal')
        if eno>5:
            if esal<7000:
                raise serializers.ValidationError('employee whose eno is greater than 5, need to have salary more than 7000')
        return data
