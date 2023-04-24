from django.db import models

from uuid import uuid4


class AbstractBaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        db_index=True, 
        default=uuid4,
        editable=False,
        unique=True,
    )
    creared_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True

