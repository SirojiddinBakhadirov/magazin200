from rest_framework import serializers
from .models import Product,\
    Firma,\
    Nakladnoy,\
    Type


class FirmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firma
        fields = "__all__"


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"


class NakladnoySerializer(serializers.ModelSerializer):
    class Meta:
        model = Nakladnoy
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

