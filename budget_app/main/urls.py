from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_income/', views.incomeform, name='incomeform'),
    path('add_expense/', views.expenseform, name='expenseform')
]
