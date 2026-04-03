from django.urls import path
from . import views

urlpatterns = [
   path('',views.dashboard,name="dashboard"),
   path('books/',views.book_list,name="booklist"),
   path("students/",views.students_list,name="students_list"),

]
