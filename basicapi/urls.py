from django.contrib import admin
from django.urls import path
from basicapi.views import BookList, BookCreate, BookDetail

urlpatterns = [
    #path('', views.book_create),
    #path('list/', views.book_list),
    #path('<int:pk>',views.books),
    path('list/', BookList.as_view()),
    path('', BookCreate.as_view()),
    path('<int:pk>', BookDetail.as_view()),

]
