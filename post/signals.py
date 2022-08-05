
from .models import Post
from django.db.models.signals import post_save
from django.dispatch import receiver
from tasks import save_post_to_models

@receiver(post_save, sender=Post)
def save_post(sender, instance, **kwargs):
    save_post_to_models.delay(instance.category.id)