from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from apps.findings import views
from apps.users.views import (
    RegistrationView, 
    AuthView,
    UserListView, 
    UserRetrieveUpdateDestroyView
)
from apps.users.views import ( 
    UserListView, 
    UserRetrieveUpdateDestroyView
    )


schema_view = get_schema_view(
    openapi.Info(
        title="Project API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



api_v1 = [
    path('', include('apps.findings.urls')),
    path('users/', UserListView.as_view(), name='profile-list'),
    path('users/<uuid:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='profile-detail'),
    path('register/', RegistrationView.as_view()),
    path('auth/', AuthView.as_view()),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),

    path('api/v1/', include(api_v1)),


]
