from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Post

'''
@receiver(post_delete, sender=Post)
def remove_file_from_s3(sender, instance, using, **kwargs):
    if instance.attachment:
        instance.attachment.delete(save=False)
    if instance.thumbnail:
        instance.thumbnail.delete(save=False)
'''

