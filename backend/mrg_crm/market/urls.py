from django.urls import path

from market.views.auth import AuthView
from market.views.product import ProductListView
from market.views.category import CategoryViewSet



urlpatterns=[

    path('userlogin', AuthView.as_view()),
    path('product_list', ProductListView.as_view()),
    # path('category_list', CategoryViewSet.as_view({'get': 'list'}))

] 