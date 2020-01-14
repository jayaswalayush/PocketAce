from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class TransactionType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=20, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Transaction Types"


class Transaction(MPTTModel):
    transaction_id = models.IntegerField(primary_key=True)
    type = models.ForeignKey(TransactionType, on_delete=models.CASCADE)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True,
                            on_delete=models.SET_NULL)
    amount = models.FloatField(max_length=50, default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} {} {}".format(self.transaction_id, self.type, self.amount)

    def get_parent_id(self):
        if self.parent:
            return self.parent.transaction_id
        else:
            return None
