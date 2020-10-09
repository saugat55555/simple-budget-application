from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.


def home(request):
    income_detail = Income.objects.all()
    expense_detail = Expense.objects.all()

    sums = Income.total_user_spend()
    expense_sum = Expense.total_user_spend()
    return render(request, 'dashboard.html',  {'income_detail': income_detail,
                                               'expense_detail': expense_detail, 'sums': sums, 'expense_sum': expense_sum})


def incomeform(request):
    if request.method == "POST":
        incomeform = IncomeForm(request.POST)
        if incomeform.is_valid():
            incomeform.save()
            return redirect('/')
    else:
        incomeform = IncomeForm()
    return render(request, 'incomeform.html', {'incomeform': incomeform})


def expenseform(request):
    if request.method == "POST":
        expenseform = ExpenseForm(request.POST)
        if expenseform.is_valid():
            expenseform.save()
            return redirect('/')
    else:
        expenseform = ExpenseForm()
    return render(request, 'expenseform.html', {'expenseform': expenseform})
