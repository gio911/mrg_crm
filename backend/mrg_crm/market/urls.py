from django.urls import path
from . import views

# from market.views1.auth import AuthView
# from market.views1.product import ProductListView
#from market.views1.category import CategoryViewSet





urlpatterns=[
    
    # path('userlogin', AuthView.as_view()),
    # path('product_list', ProductListView.as_view()),
    path('', views.CategoryListAPIView.as_view(), name='categories' ),
    path('<int:id>', views.CategoryDetailAPIView.as_view(), name='category'),
    # path('category_list', CategoryViewSet.as_view({'get': 'list'}))

] 