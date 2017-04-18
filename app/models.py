from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class NewsArticle(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name=_('Title')
    )

    short_description = models.TextField(
        verbose_name=_('Short description')
    )

    description = models.TextField(
        verbose_name=_('description')
    )
