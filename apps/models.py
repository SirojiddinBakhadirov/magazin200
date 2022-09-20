from django.db import models


class Firma(models.Model):
    name = models.CharField(max_length=200)


class Type(models.Model):
    name = models.CharField(max_length=200)


class Nakladnoy(models.Model):
    name = models.BigIntegerField()
    postavshik = models.ForeignKey(Firma, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)


class Product(models.Model):
    name = models.CharField(max_length=200)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    barcode = models.IntegerField()
    nakladnoy = models.ForeignKey(Nakladnoy, on_delete=models.CASCADE)
    amount = models.IntegerField()
    term = models.DateField(auto_created=True)
    created = models.DateField(auto_now_add=True)
    ishlab_chiqaruvchi = models.CharField(max_length=200)
    come_price = models.IntegerField()
    ustiga_foiz = models.FloatField()
    sale_price = models.IntegerField()
    pereotsenka = models.BooleanField(default=False)
    spisaniya = models.BooleanField(default=False)



