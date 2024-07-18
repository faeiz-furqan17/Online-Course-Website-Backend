from django.urls import path

from .admin import admin

from . import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('Books/', views.BookListCreate.as_view(), name='book-view-create'),
    path('Books/<int:pk>/', views.BookRetrieveUpdateDestroy.as_view(), name='book-view-detail'),
   
] 