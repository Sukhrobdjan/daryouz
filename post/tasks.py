from celery import shared_task
from .models import *

@shared_task
def save_post_to_models(category_id):

    cat = Category.objects.get(id=category_id)
    cat.post_count -= 1
    cat.save()