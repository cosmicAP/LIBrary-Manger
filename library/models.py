from django.db import models

class book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13 , unique=True)
    quantity = models.IntegerField(default=1)
    available = models.IntegerField(default=1)
    added_date = models.DateField(auto_now_add=True)



    def __str__(self):
        return self.title
    
class Students(models.Model):
    name =models.CharField( max_length=120)
    student_id = models.CharField(max_length=200,unique=True)
    email =models.EmailField(max_length=250 , unique=True,blank=True , null= True)
    phone = models.CharField (max_length=50 ,unique=True )
    joined_date = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
    
class borrowed_records(models.Model):
    book = models.ForeignKey(book, on_delete=models.CASCADE)    
    student = models.ForeignKey(Students,on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True,blank=True)
    is_returned = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.student.name} borrowed {self.book.title}   "
