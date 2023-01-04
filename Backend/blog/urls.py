from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('categories-all/', views.CategoryList.as_view()),
    path('categories/', views.CategoryListPaginated.as_view()),
    path('blogs/', views.BlogList.as_view()),
    path('categories/<int:pk>/', views.BlogCategoryList.as_view()),
    path('blogs/<int:pk>/', views.BlogDetails.as_view()),
    path('blogs/user/<int:pk>/', views.BlogUserList.as_view()),
    path('categories/<int:pk>/', views.BlogCategoryList.as_view()),
    path('categories/delete/<int:pk>/', views.CategoryDelete.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)