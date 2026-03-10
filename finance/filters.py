import django_filters
from .models import Transaction

class TransactionFilter(django_filters.FilterSet):
    created_at = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Transaction
        fields = [
            'status',
            'type',
            'category',
            'subcategory'
        ]