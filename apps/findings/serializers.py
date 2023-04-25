from rest_framework import serializers

from apps.findings.models import (
    Category,
    Finding,
    Image
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'parent',
        )


class FindingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finding
        fields = (
            'id',
            'name',
            'description',
            'price',
            'category',
            'author',
        )


class ImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            'photo',
            'is_preview',
        )
