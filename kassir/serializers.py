from .models import Kassir
from rest_framework import serializers


class KassirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kassir
        fields = "__all__"