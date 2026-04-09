from django.urls import path
from . import views

urlpatterns = [
   path('',views.dashboard,name="dashboard"),
   path('books/',views.book_list,name="book_list"),
   path('books/add/',views.book_add,name="book_add"),
   path('books/edit/<int:pk>/',views.book_edit,name="book_edit"),
   path('books/delete/<int:pk>/',views.book_delete,name="book_delete"),


  path("students/",views.students_list,name="students_list"),
  path("students/add/",views.student_add,name="student_add"),
  path("students/edit/<int:pk>/",views.student_edit,name="student_edit"),
  path("students/delete/<int:pk>/",views.student_delete,name="student_delete"),

path("borrows/", views.borrow_list, name="borrow_list"),
path("borrows/add", views.borrow_book, name="borrow_book"),
path("borrows/return/<int:pk>/", views.return_book, name="returned_book")

]
