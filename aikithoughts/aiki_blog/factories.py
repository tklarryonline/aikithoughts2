import faker
from factory.declarations import SubFactory
from factory.django import DjangoModelFactory
from factory.helpers import lazy_attribute

from .models.post import Post

fake = faker.Factory.create()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = 'auth.User'
        django_get_or_create = ('username',)

    first_name = lazy_attribute(lambda o: fake.first_name())
    last_name = lazy_attribute(lambda o: fake.last_name())
    username = lazy_attribute(lambda o: fake.user_name())
    email = lazy_attribute(lambda o: fake.email())


class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    author = SubFactory(UserFactory)
    title = lazy_attribute(lambda o: fake.sentence())
    text = lazy_attribute(lambda o: fake.text())
