from .views import KassirList, KassirDetail
from django.urls import path

urlpatterns = [
    path('', KassirList.as_view()),
    path('<int:pk>/', KassirDetail.as_view()),
]