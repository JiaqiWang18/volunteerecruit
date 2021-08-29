from __future__ import absolute_import, unicode_literals

from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.mail import send_mail

logger = get_task_logger(__name__)


@shared_task(name="celery_send_email_task")
def celery_send_email_task(subject, plain_message, user, form, html_message, fail):
    logger.info("Sent email")
    return send_mail(subject, plain_message,
                     user, form, html_message=html_message,
                     fail_silently=fail)
