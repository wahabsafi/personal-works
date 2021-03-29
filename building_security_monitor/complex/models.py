from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class Complex(models.Model):
    name=models.CharField(_("complex name"), max_length=50)
    address=models.CharField(_("complex address"), max_length=50)
    
    class Meta:
        verbose_name = _("complex")
        verbose_name_plural = _("complexs")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("complex_detail", kwargs={"pk": self.pk})



class Block(models.Model):
    complex=models.ForeignKey(Complex, verbose_name=_("complex"), on_delete=models.CASCADE)
    no=models.IntegerField(_("block number"))
    

    class Meta:
        verbose_name = _("block")
        verbose_name_plural = _("blocks")

    def __str__(self):
        return self.no

    def get_absolute_url(self):
        return reverse("block_detail", kwargs={"pk": self.pk})




class Unit(models.Model):
    block=models.ForeignKey(Block, verbose_name=_("block"), on_delete=models.CASCADE)
    no=models.IntegerField(_("unit number"))
    phone=models.CharField(_("unit phone number"), max_length=11)
    

    class Meta:
        verbose_name = _("Unit")
        verbose_name_plural = _("Units")

    def __str__(self):
        return self.no

    def get_absolute_url(self):
        return reverse("Unit_detail", kwargs={"pk": self.pk})
