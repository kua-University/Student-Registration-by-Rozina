from django import forms
from .models import StudentInfo

class CreateStudent(forms.ModelForm):
    class Meta:
        model = StudentInfo
        exclude = ("student_img", "fathers_img", "mothers_img", )

        widgets = {
            'academic_year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 2010'}),
            'admission_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 2010-02-01' ,'type': 'date'}),
            'admission_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: UGR/000000/10'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Abebe Kebede'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 19'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'class_type': forms.Select(attrs={'class': 'form-control'}),
            'section_type': forms.Select(attrs={'class': 'form-control'}),
            'shift_type': forms.Select(attrs={'class': 'form-control'}),
            'fathers_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Kebede Abera'}),
            'fathers_nid': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 3732106814'}),
            'fathers_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 01884334899'}),
            'mothers_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Abrehet Gebre'}),
            'mothers_nid': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 3732106814'}),
            'mothers_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 01884334899'}),
        }

