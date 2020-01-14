from django.urls import path

from transaction import views

urlpatterns = [

    path('transaction/<int:transaction_id>/', views.TransactionView.as_view(), name='transaction'),

    path('types/<str:type_slug>/', views.TransactionsView.as_view(), name='filter-transaction'),

    path('sum/<int:transaction_id>/', views.TransactionSumView.as_view(), name='transaction-sum'),

    path('types/', views.TransactionTypeView.as_view(), name='transaction-types'),
]
