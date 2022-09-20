from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import FirmaSerializer,\
    TypeSerializer,\
    NakladnoySerializer,\
    ProductSerializer
from .models import Firma,\
    Type,\
    Nakladnoy,\
    Product


class FirmaList(ListCreateAPIView):
    queryset = Firma.objects.all()
    serializer_class = FirmaSerializer


class FirmaDetail(RetrieveUpdateDestroyAPIView):
    queryset = Firma.objects.all()
    serializer_class = FirmaSerializer


class TypeList(ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class TypeDetail(RetrieveUpdateDestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class NakladnoyList(ListCreateAPIView):
    queryset = Nakladnoy.objects.all()
    serializer_class = NakladnoySerializer


class NakladnoyDetail(RetrieveUpdateDestroyAPIView):
    queryset = Nakladnoy.objects.all()
    serializer_class = NakladnoySerializer


class ProductList(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        params = self.request.query_params

        pereotsenka = params.get('pereotsenka', None)

        if pereotsenka:
            queryset = queryset.filter(pereotsenka=True)
            return queryset
        else:
            return queryset


class ProductDetail(APIView):
    def get_object(self, id):
        return Product.objects.get(id=id)

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def patch(self, request, pk):
        product_object = self.get_object(pk)
        serializer = ProductSerializer(product_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            Product.objects.filter(pk=pk).update(pereotsenka=True)
            return JsonResponse(data=serializer.data)
        return JsonResponse(data='error')

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return HttpResponse('delete')


def get_product_by_barcode(request):
    response = {
        'success': False,
        'data': []
    }
    try:
        will_get = request.GET['barcode']
        lists = list(Product.objects.filter(barcode=will_get))
        response['success'] = True
        for obj in lists:
            response['data'].append({
                'id': int(obj.id),
                'name': str(obj.name),
                'nakladnoy': int(obj.nakladnoy.name),
                'term': str(obj.term),
                'created': str(obj.created)
            })
    except:
        response['success'] = False
        print('bad')

    finally:
        return JsonResponse(response, safe=False)


def search_product_name(request):
    response = {
        'success': False,
        'data': []
    }
    try:
        will_get = request.GET['name']
        lists = list(Product.objects.filter(name=will_get))
        response['success'] = True
        for obj in lists:
            response['data'].append({
                'id': int(obj.id),
                'barcode': int(obj.barcode),
                'nakladnoy': int(obj.nakladnoy.name),
                'term': str(obj.term),
                'created': str(obj.created),
            })
    except:
        response['success'] = False
        print('bad')

    finally:
        return JsonResponse(response, safe=False)
