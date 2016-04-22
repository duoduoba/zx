__author__ = 'zx'
# coding£ºutf-8
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import SpendDetail


@receiver(post_delete, sender=SpendDetail)
def photo_post_delete_handler(sender, **kwargs):
    detail = kwargs['instance']
    print(detail)
    for index in range(1, 5):
        image_name = 'image' + str(index)
        print(image_name)
        image_path = detail.__dict__[image_name]
        image_path = image_path.replace('/', '\\')
        import os
        from zx.settings import MEDIA_ROOT
        image_path = MEDIA_ROOT + '\\' + image_path
        print(image_path)
        if os.path.isfile(image_path):
            os.remove(image_path)