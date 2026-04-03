from django.shortcuts import render
from .models import book , Students ,borrowed_records
def dashboard(request):
    total_books = book.objects.count()
    total_students = Students.objects.count()
    total_borrows = borrowed_records.objects.filter(is_returned=False).count()
    
    context = {
        'total_books':total_books,
        'total_students': total_students,
        'total_books_borrwed' : total_borrows
    }
    return render(request , 'library/dashboard.html',context)

def book_list(request):
    books = book.objects.all()
    context = { 
        'books':books
    }
    return render(request , 'library/book_list.html',context)


def students_list(request):
    students_all= Students.objects.all() 
    context = {
        'Students': students_all
    }   
    return render(request , 'library/student_list.html',context)
