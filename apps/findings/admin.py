from django.contrib import admin


from apps.findings.models import (
    Category,
    Finding,
    Image
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Finding)
class FindingAdmin(admin.ModelAdmin):
    pass


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
