from django import forms
from first.models import Student
class StudentForm(forms.ModelForm):
    def clean_marks(self):
        inputmarks = self.cleaned_data.get('marks')
        if inputmarks<40:
            raise forms.ValidationError('The minimum required marks is 40')
        return inputmarks
        
    class Meta:
        model = Student
        fields = '__all__'
