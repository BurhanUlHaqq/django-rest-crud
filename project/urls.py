
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions

from app import urls as app_url
from web_interface import urls as web_url

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Your API Title",
        default_version='v1',
        description="Test description for your API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="your-email@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/apis/', include(app_url)),
    path('', include(web_url)),
]

urlpatterns = urlpatterns +[
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # Other URL patterns for your APIs
]


