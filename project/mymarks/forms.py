from django import forms

from .models import Students


class StudentsModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields =[
            'name',
            'mail',
            'school',
            'level',
            'password',
            'fiscul',
            'lit',
            'algebra',
            'geomet',
            'history',
            'obg',
            'fiscul_t',
            'lit_t',
            'algebra_t',
            'geomet_t',
            'history_t',
            'obg_t',
        ]

     