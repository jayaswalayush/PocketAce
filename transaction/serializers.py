from rest_framework import serializers

from transaction.models import Transaction, TransactionType


class TransactionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionType
        fields = (
            'id', 'name', 'slug')


class TransactionSerializer(serializers.ModelSerializer):
    type = serializers.StringRelatedField(source='type.slug')
    parent_id = serializers.SerializerMethodField()

    def get_parent_id(self, obj):
        return obj.get_parent_id()

    class Meta:
        model = Transaction
        fields = ('amount', 'type', 'parent_id')
