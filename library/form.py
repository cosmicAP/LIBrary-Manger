from django import forms
from .models import book , Students , borrowed_records

class BookForm(forms.ModelForm):
    class Meta:
        model = book
        fields = ['title','author','isbn','quantity','available']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name','student_id','email','phone']

class BorrowedForm(forms.ModelForm):
    class Meta:
        models = borrowed_records
        fields = ['book','student']
              