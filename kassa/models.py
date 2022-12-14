from django.db import models

from apps.models import Nakladnoy
from kassir.models import Kassir


class Arxiv(models.Model):
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=200)
    product_type = models.CharField(max_length=200)
    product_barcode = models.IntegerField()
    nakladnoy = models.BigIntegerField
    amount = models.IntegerField()
    term = models.BigIntegerField
    cost = models.IntegerField()
    summa = models.BigIntegerField()
    sold = models.DateField(auto_now_add=True)
    user = models.ForeignKey(Kassir, on_delete=models.CASCADE)
