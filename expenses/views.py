

from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense

def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expenses/list.html', {'expenses': expenses})


def add_expense(request):
    if request.method == 'POST':
        Expense.objects.create(
            amount=request.POST['amount'],
            category=request.POST['category'],
            date=request.POST['date'],
            description=request.POST.get('description', '')
        )
        return redirect('expense_list')

    return render(request, 'expenses/add.html')


def edit_expense(request, id):
    expense = get_object_or_404(Expense, id=id)

    if request.method == 'POST':
        expense.amount = request.POST['amount']
        expense.category = request.POST['category']
        expense.date = request.POST['date']
        expense.description = request.POST.get('description', '')
        expense.save()
        return redirect('expense_list')

    return render(request, 'expenses/edit.html', {'expense': expense})


def delete_expense(request, id):
    expense = get_object_or_404(Expense, id=id)
    expense.delete()
    return redirect('expense_list')

