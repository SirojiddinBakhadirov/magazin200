from django.urls import path, include
from .views import FirmaList,\
    FirmaDetail,\
    TypeList,\
    TypeDetail,\
    NakladnoyList,\
    NakladnoyDetail,\
    ProductList,\
    ProductDetail,\
    search_product_name,\
    get_product_by_barcode, Spisaniya

urlpatterns = [
    path('kassir/', include('kassir.urls')),

    path('firma/', FirmaList.as_view()),
    path('firma/<int:pk>/', FirmaDetail.as_view()),

    path('type/', TypeList.as_view()),
    path('type/<int:pk>/', TypeDetail.as_view()),

    path('nakladnoy/', NakladnoyList.as_view()),
    path('nakladnoy/<int:pk>/', NakladnoyDetail.as_view()),

    path('product/', ProductList.as_view()),
    path('product/<int:pk>/', ProductDetail.as_view()),

    path('spisaniya/<int:pk>/', Spisaniya.as_view()),

    path('search_name/', search_product_name),
    path('search_barcode/', get_product_by_barcode),
]