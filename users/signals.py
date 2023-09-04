from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from blog.models import Post


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=Post)
def create_post_img(sender, instance, created, **kwargs):
    if created:
        Post.objects.create(post=instance)


@receiver(post_save, sender=Post)
def save_post_img(sender, instance, created, **kwargs):
    instance.post.save()