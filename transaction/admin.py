from django.contrib import admin

from transaction.models import Transaction, TransactionType


class TransactionTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'type', 'parent', 'amount', 'created_on')
    list_filter = ['type']
    search_fields = ['type', 'transaction_id','parent__id']


admin.site.register(TransactionType, TransactionTypeAdmin)
admin.site.register(Transaction, TransactionAdmin)
