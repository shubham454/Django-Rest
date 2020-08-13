from rest_framework import serializers
from testapp.models import Employee


# validation by using validators
def multiple_of_1000(value):
    print('validation by using validators')
    if value % 1000 != 0:
        raise serializers.ValidationError('Salary should be multiple of 1000')

class EmployeeSerializer(serializers.ModelSerializer):
    esal = serializers.FloatField(validators=[multiple_of_1000])

    class Meta:
        model = Employee
        fields = '__all__'

    def validate_esal(self, value):
        # this is a field level validation for databases
        if value < 5000:
            raise serializers.ValidationError('Employee salary should be greater than 5000')
        return value

    def validate(self, data):
        # this is object level validation for the databasses
        ename = data.get('ename')
        esal = data.get('esal')
        if ename.lower() == 'sunny':
            if esal < 60000:
                raise serializers.ValidationError('sunny salary should be greater than 60000')
        return data
