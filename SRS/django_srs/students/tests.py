from django.test import TestCase
from .forms import CreateStudent
from .models import StudentClassInfo, StudentSectionInfo, StudentShiftInfo, StudentInfo, Attendance
from django.db import IntegrityError

#unit testing
class TestCreateStudentForm(TestCase):
    def test_valid_form(self):
        data = {
            'academic_year': '2022',
            'admission_date': '2022-01-01',
            'admission_id': 'UGR/123456/10',
            'name': 'John Doe',
            'age': 20,
            'gender': 'male',
            'class_type': 'Year l',
            'section_type': 'Section A',
            'shift_type': 'Morning Shift',
            'fathers_name': 'John Smith',
            'fathers_nid': '12345678',
            'fathers_number': '0188438099',
            'mothers_name': 'Jane Doe',
            'mothers_nid': '87654321',
            'mothers_number': '0188433999',
        }
        form = CreateStudent(data)
        self.assertTrue(form.is_valid())

    def test_invalid_academic_year(self):
        data = {
            'academic_year': 'abc',  # invalid year
            'admission_date': '2022-01-01',
            'admission_id': 'UGR/123456/10',
            'name': 'John Doe',
            'age': 20,
            'gender': 'male',
            'class_type': 'class1',
            'section_type': 'section1',
            'shift_type': 'morning',
            'fathers_name': 'John Smith',
            'fathers_nid': '12345678',
            'fathers_number': '01884334899',
            'mothers_name': 'Jane Doe',
            'mothers_nid': '87654321',
            'mothers_number': '01884334899',
        }
        form = CreateStudent(data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['academic_year'], ['Invalid academic year. Must be a 4-digit year.'])

    def test_invalid_admission_date(self):
        data = {
            'academic_year': '2022',
            'admission_date': '2026-01-01',  # invalid date (in the future)
            'admission_id': 'UGR/123456/10',
            'name': 'John Doe',
            'age': 20,
            'gender': 'male',
            'class_type': 'class1',
            'section_type': 'section1',
            'shift_type': 'morning',
            'fathers_name': 'John Smith',
            'fathers_nid': '12345678',
            'fathers_number': '1884334899',
            'mothers_name': 'Jane Doe',
            'mothers_nid': '87654321',
            'mothers_number': '1884334899',
        }
        form = CreateStudent(data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['admission_date'], ['Invalid admission date. Must be a date in the past.'])

#integration testing
class TestStudentInfoModel(TestCase):
    def test_create_student_info(self):
        student_class_info = StudentClassInfo.objects.create(class_name='Class 1', class_short_form='C1')
        student_section_info = StudentSectionInfo.objects.create(section_name='Section 1')
        student_shift_info = StudentShiftInfo.objects.create(shift_name='Morning Shift')
        student_info = StudentInfo.objects.create(
            academic_year='2022',
            admission_date='2022-01-01',
            admission_id='S1',
            name='John Doe',
            age=20,
            gender='male',
            class_type=student_class_info,
            section_type=student_section_info,
            shift_type=student_shift_info,
            fathers_name='John Smith',
            fathers_nid=12345678,
            fathers_number=1234567890,
            mothers_name='Jane Doe',
            mothers_nid=98765432,
            mothers_number=9876543210,
        )
        self.assertEqual(student_info.academic_year, '2022')
        self.assertEqual(student_info.admission_date, '2022-01-01')
        self.assertEqual(student_info.admission_id, 'S1')
        self.assertEqual(student_info.name, 'John Doe')
        self.assertEqual(student_info.age, 20)
        self.assertEqual(student_info.gender, 'male')
        self.assertEqual(student_info.class_type, student_class_info)
        self.assertEqual(student_info.section_type, student_section_info)
        self.assertEqual(student_info.shift_type, student_shift_info)


    def test_unique_together(self):
        student_class_info = StudentClassInfo.objects.create(class_name='Class 1', class_short_form='C1')
        StudentInfo.objects.create(
            academic_year='2022',
            admission_date='2022-01-01',
            admission_id='S1',
            name='John Doe',
            age=20,
            gender='male',
            class_type=student_class_info,
            section_type=StudentSectionInfo.objects.create(section_name='Section 1'),
            shift_type=StudentShiftInfo.objects.create(shift_name='Morning Shift'),
            fathers_name='John Smith',
            fathers_nid=12345678,
            fathers_number=1234567890,
            mothers_name='Jane Doe',
            mothers_nid=98765432,
            mothers_number=9876543210,
        )
        with self.assertRaises(IntegrityError):
            StudentInfo.objects.create(
                academic_year='2022',
                admission_date='2022-01-01',
                admission_id='S1',
                name='Jane Doe',
                age=20,
                gender='female',
                class_type=student_class_info,
                section_type=StudentSectionInfo.objects.create(section_name='Section 1'),
                shift_type=StudentShiftInfo.objects.create(shift_name='Morning Shift'),
                fathers_name='John Smith',
                fathers_nid=12345678,
                fathers_number=1234567890,
                mothers_name='Jane Doe',
                mothers_nid=98765432,
                mothers_number=9876543210,
            )

