from django.contrib import admin
from django.urls import path, include

from transaction import urls as transaction_urls

urlpatterns = [
    path('admin/', admin.site.urls),

    path('transactionservice/', include(transaction_urls)),
]
