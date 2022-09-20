from .models import Kassir
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import KassirSerializer


class KassirList(ListCreateAPIView):
    queryset = Kassir.objects.all()
    serializer_class = KassirSerializer


class KassirDetail(RetrieveUpdateDestroyAPIView):
    queryset = Kassir.objects.all()
    serializer_class = KassirSerializer

