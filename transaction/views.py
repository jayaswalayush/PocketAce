import logging

from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from transaction.models import TransactionType, Transaction
from transaction.serializers import TransactionTypeSerializer, TransactionSerializer

log = logging.getLogger(__name__)


class TransactionView(RetrieveAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()

    def get_object(self):
        return Transaction.objects.get(pk=self.kwargs['transaction_id'])

    def put(self, request, transaction_id):
        try:
            if Transaction.objects.filter(transaction_id=transaction_id).exists():
                return Response({"success": False, "message": "A transaction already exists with the provided transaction id"},
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                parent = None
                amount = request.data.get('amount', 0.0)
                type_slug = request.data.get('type', '')
                parent_id = request.data.get('parent_id', '')
                if TransactionType.objects.filter(slug=type_slug).exists():
                    transaction_type = TransactionType.objects.get(slug=type_slug)
                    if parent_id:
                        parent = Transaction.objects.get(transaction_id=parent_id)
                    Transaction.objects.create(transaction_id=transaction_id, type=transaction_type, parent=parent, amount=amount)
                else:
                    return Response(
                        {"success": False, "message": "Invalid transaction type"}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"success": True, "message": "Transaction has been saved successfully"})
        except Exception as ex:
            log.error("TransactionView || An error occurred. Please try again , Exception :" + str(ex))
            return Response({"success": False, "message": "An error occurred. Please try again", "exception": str(ex)},
                            status=status.HTTP_400_BAD_REQUEST)


class TransactionsView(APIView):

    def get(self, request, type_slug):
        try:
            transactions = []
            query_set = Transaction.objects.filter(type__slug=type_slug).values('transaction_id')
            for data in query_set:
                transactions.append(data['transaction_id'])
            return Response(transactions)
        except Exception as ex:
            log.error("TransactionsView || An error occurred. Please try again , Exception :" + str(ex))
            return Response({"success": False, "message": "An error occurred. Please try again", "exception": str(ex)},
                            status=status.HTTP_400_BAD_REQUEST)


class TransactionSumView(APIView):

    def get(self, request, transaction_id):
        try:
            if Transaction.objects.filter(transaction_id=transaction_id).exists():
                transaction = Transaction.objects.get(pk=transaction_id)
                transaction_sum = transaction.amount
                query_set = transaction.get_descendants().values('amount')
                for data in query_set:
                    transaction_sum += data['amount']
                return Response({"sum": transaction_sum})
            else:
                return Response({"sum": False, "message": "Invalid transaction id"},
                                status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            log.error("TransactionsView || An error occurred. Please try again , Exception :" + str(ex))
            return Response({"success": False, "message": "An error occurred. Please try again", "exception": str(ex)},
                            status=status.HTTP_400_BAD_REQUEST)


class TransactionTypeView(ListAPIView):
    serializer_class = TransactionTypeSerializer

    def get_queryset(self):
        return TransactionType.objects.all().order_by('name')
