from django.shortcuts import render

# list expenses
def index(request):
    return render(request, 'expenses/index.html')

# add expenses
def add_expense(request):
    return render(request, 'expenses/add_expense.html')