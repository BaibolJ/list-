from django import forms
from .models import Enrollment


class EnrollmentCreateForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = (
            'course',
            'course_time',
            'course_day',
            'course_duration',
            'is_teens',
            'price',
            'status'
        )


class EnrollmentUpeForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = (
            'course',
            'course_time',
            'course_day',
            'course_duration',
            'is_teens',
            'price',
            'status'
        )




        