from django import forms
from .models import Book , Students , BorrowedRecords

class BookForm(forms.ModelForm):
    class Meta:
      model = Book
      fields  = ['title', 'author', 'isbn', 'quantity', 'available']
    
 
 
class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'student_id', 'email', 'phone']
 

class BorrowForm(forms.ModelForm):
    
    class Meta:
        model = BorrowedRecords
        fields = ['book', 'student']