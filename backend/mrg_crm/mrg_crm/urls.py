
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from rest_framework import permissions, routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



# from market.views1.category import CategoryViewSet
# from market.views1.auth import AuthView

schema_view = get_schema_view(
   openapi.Info(
      title="Delivery",
      default_version='v',
      description='''
      Documentation `RedDoc` view can be found [here](/doc)
      ''',
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
# router.register(r'category', CategoryViewSet )


urlpatterns = [

    path('admin/', admin.site.urls),
    path('v1/', include([
        path('viewsets/', include(router.urls)), #VIEWSETS ROUTS
        path('categories/', include('market.urls')), #GENERIC ROUTS
        
    ])),
    path('api/', include('users.urls')),
    # path('api/token/', TokenObtainPairView.as_view()),
    # path('api/token/refresh/', TokenRefreshView.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


from django.conf import settings
from django.conf.urls.static import static

urlpatterns += [] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
