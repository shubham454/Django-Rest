from rest_framework import serializers
from .models import Employee

def multiple_of_1000(value):
    print('validation by using validators')
    if value%1000!=0:
        raise serializers.ValidationError('Salary should be multiple of 1000')

class EmployeeSerializer(serializers.Serializer):
    eno = serializers.IntegerField()
    ename = serializers.CharField()
    esal = serializers.FloatField(validators=[multiple_of_1000])
    eaddr = serializers.CharField()

    def validate_esal(self,value):
        # this is a field level validation for databases
        if value<5000:
            raise serializers.ValidationError('Employee salary should be greater than 5000')
        return value
    def validate(self,data):
        # this is object level validation for the databasses
        ename=data.get('ename')
        esal=data.get('esal')
        if ename.lower()=='sunny':
            if esal<60000:
                raise serializers.ValidationError('sunny salary should be greater than 60000')
        return data

    def create(self,validated_data):
        # we have to override create methd in serializer class to post or pudate data
        return Employee.objects.create(**validated_data)
    def update(self,instance,validated_data):
        instance.eno=validated_data.get('eno',instance.eno)
        instance.ename=validated_data.get('ename',instance.ename)
        instance.esal=validated_data.get('esal',instance.esal)
        instance.eaddr=validated_data.get('eaddr',instance.eaddr)
        instance.save()
        return instance
