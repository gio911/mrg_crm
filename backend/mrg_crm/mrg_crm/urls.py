
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from rest_framework import permissions, routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from market.views.category import CategoryViewSet
from market.views.auth import AuthView

schema_view = get_schema_view(
   openapi.Info(
      title="Delivery",
      default_version='v1',
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
router.register(r'category', CategoryViewSet )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include([
        path('viewsets/', include(router.urls)), #VIEWSETS ROUTS
        path('generic/', include('market.urls')) #GENERIC ROUTS
    ])
        ),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


from django.conf import settings
from django.conf.urls.static import static

urlpatterns += [] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
