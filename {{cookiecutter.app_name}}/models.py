from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.db import models

from django_extensions.db.models import TimeStampedModel


class {{ cookiecutter.model_name }}(TimeStampedModel):
    name = models.CharField(
        verbose_name=_('name'),
        max_length=255,
        blank=True,
        null=True,
    )
