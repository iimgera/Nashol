from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.findings.models import Finding, Category
from apps.findings.serializers import (
    FindingSerializer,
    CategorySerializer,
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class FindingViewSet(viewsets.ModelViewSet):
    queryset = Finding.objects.all()
    serializer_class = FindingSerializer
    permission_classes = [IsAuthenticated]
