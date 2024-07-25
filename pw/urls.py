from django.contrib import admin
from django.urls import path
from pw.views import product_list, product_detail

urlpatterns=[
    path("pl/", product_list, name="product_list"),
    path("pd/<int:product_id", product_detail, name="product_detail")
]