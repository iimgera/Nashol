from rest_framework import (
    generics, 
    viewsets
)
from rest_framework import permissions
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)

from apps.findings.models import (
    Finding,
    Category
)
from apps.findings.serializers import (
    FindingSerializer,
    CategorySerializer,
)


app_name = 'findings'

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
 

class CategoryCreateAPIView(generics.CreateAPIView):
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
 

class CategoryRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
 

class CategoryUpdateAPIView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
 

class CategoryDestroyAPIView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
 

class FindingListAPIView(generics.ListAPIView):
    queryset = Finding.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = FindingSerializer
 

class FindingCreateAPIView(generics.CreateAPIView):
    queryset = Finding.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = FindingSerializer
 

class FindingRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Finding.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = FindingSerializer
 

class FindingUpdateAPIView(generics.UpdateAPIView):
    queryset = Finding.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = FindingSerializer
 

class FindingDestroyAPIView(generics.DestroyAPIView):
    queryset = Finding.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = FindingSerializer
 



