from django import forms
from .models import TeacherInfo

class CreateTeacher(forms.ModelForm):
    class Meta:
        model = TeacherInfo
        fields = "__all__"

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Solomon Daniel '}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ex: solomon@gmail.com'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 35'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'teacher_img': forms.FileInput(attrs={'class': 'form-control'}),
            'passing_year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 2010-2015'}),
            'joining_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 2009-09-10'}),
            'admission_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: INS/003/09'}),
            'dept_type': forms.Select(attrs={'class': 'form-control'}),
            'sub_type': forms.Select(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 8999.99'}),
        }