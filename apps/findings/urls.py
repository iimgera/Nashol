from django.urls import path, include

from apps.findings.views import (
    CategoryListAPIView,
    CategoryCreateAPIView,
    CategoryRetrieveAPIView,
    CategoryUpdateAPIView,
    CategoryDestroyAPIView,
    FindingListAPIView,
    FindingCreateAPIView,
    FindingRetrieveAPIView,
    FindingUpdateAPIView,
    FindingDestroyAPIView,
)


urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('categories/create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('categories/<uuid:pk>/', CategoryRetrieveAPIView.as_view(), name='category-detail'),
    path('categories/<uuid:pk>/update/', CategoryUpdateAPIView.as_view(), name='category-update'),
    path('categories/<uuid:pk>/delete/', CategoryDestroyAPIView.as_view(), name='category-delete'),

    path('findings/', FindingListAPIView.as_view(), name='finding-list'),
    path('findings/create/', FindingCreateAPIView.as_view(), name='finding-create'),
    path('findings/<uuid:pk>/', FindingRetrieveAPIView.as_view(), name='finding-detail'),
    path('findings/<uuid:pk>/update/', FindingUpdateAPIView.as_view(), name='finding-update'),
    path('findings/<uuid:pk>/delete/', FindingDestroyAPIView.as_view(), name='finding-delete'),
]

