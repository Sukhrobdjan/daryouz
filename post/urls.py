from django.urls import path
from . import views

urlpatterns = [
    path('news/<str:slug>/', views.CategoryView.as_view(), name="all_news"),
    ]