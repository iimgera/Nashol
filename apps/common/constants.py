from django.db.models import TextChoices


class UserType(TextChoices):
    PRODUCER = 'PRODUCER'
    CONSUMER = 'CONSUMER'
    

