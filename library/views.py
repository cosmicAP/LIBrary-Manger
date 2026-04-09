from django.shortcuts import render , redirect , get_object_or_404
from .models import Book , Students ,BorrowedRecords
from .forms import BookForm , StudentForm , BorrowForm
def dashboard(request):
    total_books = Book.objects.count()
    total_students = Students.objects.count()
    total_borrows = BorrowedRecords.objects.filter(is_returned=False).count()
    
    context = {
        'total_books':total_books,
        'total_students': total_students,
        'total_books_borrwed' : total_borrows
    }
    return render(request , 'library/dashboard.html',context)


##this will show the books

def book_list(request):
    books = Book.objects.all()
    context = { 
        'books':books
    }
    return render(request , 'library/book_list.html',context)

def book_add(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request,'library/book_form.html',{'form':form})        
    
def book_edit(request,pk):
    book = get_object_or_404(Book,pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST , instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request,'library/book_form.html',{'form':form} )

def book_delete(request,pk):
    book = get_object_or_404(Book,pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    
    return render (request , 'library/book_confirm_delete.html',{'book':book})        
    

#student view

def students_list(request):
    students_all= Students.objects.all() 
    context = {
        'Students': students_all
    }   
    return render(request , 'library/student_list.html',context)

def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students_list')
    else:
        form = StudentForm()
    return render (request , 'library/student_form.html',{'form':form})

def student_edit(request, pk):
    student = get_object_or_404(Students, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'library/student_form.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Students, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('students_list')
    return render(request, 'library/student_delete.html', {'student': student})



#borrowing system#

def borrow_book(request):
    if request.method == "POST":
        form = BorrowForm(request.POST)
        if form.is_valid():
            borrow = form.save(commit=False)
            book = borrow.book
            if book.available > 0:
                book.available -= 1
                book.save()
                borrow.save()
                return redirect ('borrow_list')
            else:
                form.add_error('book','This Book is not available to us!!')

    else:
        form = BorrowForm()
    return render (request , "library/borrow_form.html",{'form':form}) 

def borrow_list(request):
    borrows = BorrowedRecords.objects.filter(is_returned=False)  
    return render (request , 'library/borrow_list.html',{'borrows':borrows})

def return_book(request,pk):
    borrow = get_object_or_404(BorrowedRecords,pk=pk)
    if request.method == 'POST':
        borrow.is_returned = True
        borrow.save()
        book = borrow.book
        book.available +=1
        book.save()
        return redirect ('borrow_list')
    return render (request , 'library/return_confirm.html',{'borrow': borrow})

