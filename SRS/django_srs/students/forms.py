from django import forms
from .models import StudentInfo
from datetime import datetime
class CreateStudent(forms.ModelForm):
    class Meta:
        model = StudentInfo
        exclude = ("student_img", "fathers_img", "mothers_img", )

        widgets = {
            'academic_year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 2010'}),
            'admission_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 2010-02-01', 'type': 'date'}),
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

    def clean_academic_year(self):
        academic_year = self.cleaned_data['academic_year']
        if len(str(academic_year)) != 4:
            raise forms.ValidationError('Invalid academic year. Must be a 4-digit year.')
        return academic_year

    def clean_admission_date(self):
        admission_date = self.cleaned_data['admission_date']
        if admission_date > datetime.now().date():
            raise forms.ValidationError('Invalid admission date. Must be a date in the past.')
        return admission_date

    def clean_admission_id(self):
        admission_id = self.cleaned_data['admission_id']
        if len(admission_id) < 6:
            raise forms.ValidationError('Invalid admission ID. Must be at least 6 characters long.')
        return admission_id

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 0:
            raise forms.ValidationError('Invalid age. Must be a non-negative integer.')
        return age

    def clean_fathers_nid(self):
        fathers_nid = self.cleaned_data['fathers_nid']
        if len(str(fathers_nid)) != 8:
            raise forms.ValidationError('Invalid father\'s NID. Must be a 8-digit number.')
        return fathers_nid

    def clean_fathers_number(self):
        fathers_number = self.cleaned_data['fathers_number']
        if len(str(fathers_number)) != 10:
            raise forms.ValidationError('Invalid father\'s phone number. Must be  10-digit number.')
        return fathers_number

    def clean_mothers_nid(self):
        mothers_nid = self.cleaned_data['mothers_nid']
        if len(str(mothers_nid)) != 8:
            raise forms.ValidationError('Invalid mother\'s NID. Must be a 8-digit number.')
        return mothers_nid

    def clean_mothers_number(self):
        mothers_number = self.cleaned_data['mothers_number']
        if len(str(mothers_number)) != 10:
            raise forms.ValidationError('Invalid mother\'s phone number. Must be  10-digit number.')
        return mothers_number