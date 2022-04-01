from django.urls import path
from . import views

# from market.views1.auth import AuthView
# from market.views1.product import ProductListView
#from market.views1.category import CategoryViewSet





urlpatterns=[
    #http://localhost:8000/api/categories/
    # path('userlogin', AuthView.as_view()),
    # path('product_list', ProductListView.as_view()),
    path('categories/', views.CategoryListAPIView.as_view(), name='categories' ),
    path('categories/<int:id>/', views.CategoryDetailAPIView.as_view(), name='category'),
    path('product_list/<int:id>/', views.ProductListView.as_view()),
    path('add_product/', views.AddProductView.as_view(), name='add-product'),
    path('add_product/<int:id>/', views.AddProductView.as_view(), name='add-product'),
    path('delete_product/<int:id>/', views.AddProductView.as_view(), name = 'delete-product'),
    path('order_submit/', views.BasketSubmitView.as_view()), 
    # path('category_list', CategoryViewSet.as_view({'get': 'list'}))

] 