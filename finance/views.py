from django.shortcuts import render, redirect, get_object_or_404
from .models import Transaction
from .forms import TransactionForm
from .filters import TransactionFilter

def transaction_list(request):
    qs = Transaction.objects.all().order_by('-created_at')

    transaction_filter = TransactionFilter(request.GET, queryset=qs)

    return render(
        request,
        'transactions_list.html',
        {
            'filter': transaction_filter
        }
    )

def transaction_create(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('transactions')
    else:
        form = TransactionForm()

    return render(
        request,
        'transiction_form.html',
        {
            'form': form
        }
    )

def transiction_update(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)

    if request.method == "POST":
        form = TransactionForm(request.POST, pk=pk)

        if form.is_valid():
            form.save()
            return redirect('transactions')
    else:
        form = TransactionForm(instance=transaction)

    return render(
        request,
        'transaction_form.html',
        {
            'form': form
        }
    )

def transaction_delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)

    transaction.delete()

    return redirect('transactions')
