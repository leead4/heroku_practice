import factory
from blogpost.models.models import *
from django.contrib.auth.models import *

# class TagsFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Tags
#     topic = factory.Faker('name')

# class AnimationFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Animation
#     style = factory.Faker('bs')


class ContentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Content
    text = factory.Faker('bs')

class AssetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Asset
    animation = factory.SubFactory('blogpost.factories.AnimationFactory')
    # image_author = factory.SubFactory('blogpost.factories.AssetFactory')

# class ContentAssetFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = ContentAsset
#     asset = factory.SubFactory('blogpost.factories.AssetFactory')
#     content = factory.SubFactory('blogpost.factories.ContentFactory')

class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author
    name = factory.Faker('first_name')
    avatar = factory.SubFactory('blogpost.factories.AssetFactory')


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post
    content = factory.SubFactory('blogpost.factories.ContentFactory')
    title = factory.Faker('bs')
    post_like = factory.Faker('random_int', min=100, max=300)
    post_type = "Illustration"
    date = factory.Faker('date')
    post_author = factory.Iterator(Author.objects.all())

   
# class PostTagFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = PostTag
#     tag = factory.SubFactory(TagsFactory)
#     post = factory.SubFactory(PostFactory)




