from django import forms
from testapp.models import Employee

class EmployeeForm(forms.ModelForm):
    def clean_esal(self):
        inputsal = self.cleaned_data.get('esal')
        if inputsal < 2000:
            raise forms.ValidationError('minimum salary should be 2000')
        return inputsal
    class Meta:
        model = Employee
        fields = '__all__'
