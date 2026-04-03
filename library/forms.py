from django import forms
from .models import book , Students , borrowed_records

class BookForm(forms.ModelForm):
    class meta:
      model =book
      fields  = ['title', 'author', 'isbn', 'quantity', 'available']
    
 
 
class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'student_id', 'email', 'phone']
 

class BorrowForm(forms.ModelForm):
    
    class Meta:
        model = borrowed_records
        fields = ['book', 'student']