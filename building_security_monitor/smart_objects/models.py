from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Lock(models.Model):
    """Model definition for Lock."""

    is_open=models.BooleanField(_("open status"))
    last_opened=models.TimeField(_("last time opened"), auto_now=True)
    password=models.CharField(_("lock password"), max_length=50)
    

    class Meta:
        """Meta definition for Lock."""

        verbose_name = 'Lock'
        verbose_name_plural = 'Locks'

    def __str__(self):
        """Unicode representation of Lock."""
        pass
