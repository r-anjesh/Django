from django import forms
from .models import employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = employee
        fields = ['emp_name', 'login_time', 'logout_time']