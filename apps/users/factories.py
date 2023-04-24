import factory
from faker import Faker

from apps.users.models import User


fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.LazyAttribute(lambda x: fake.unique.user_name())
    email = factory.LazyAttribute(lambda x: fake.email())
    password = factory.PostGenerationMethodCall('set_password', 'password')