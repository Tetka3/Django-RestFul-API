from django.urls import path
from . import views 

urlpatterns = [
    path('', views.book_list),
    path('books/<int:id>/', views.book_detail)
]