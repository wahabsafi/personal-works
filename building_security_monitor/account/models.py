from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


# Create your models here.



class User(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        )
    ROLE_CHOICES = (
        ('F', 'Father'),
        ('M', 'Mother'),
        ('S', 'Son'),
        ('D', 'Daughter'),
        )
    gender = models.CharField(_("Gender"),max_length=1, choices=GENDER_CHOICES,default='M')
    birth_day=models.DateField(_("Birthday"),blank=True,null=True)
    family=models.ForeignKey("family.Family", verbose_name=_("family"),blank=True,null=True, on_delete=models.SET_NULL)
    role=models.CharField(_("Role in family"),max_length=1,blank=True, choices=ROLE_CHOICES)
    phone=models.CharField(_("phone number"), max_length=11,blank=True)
    is_owner=models.BooleanField(_("owner status"),default=False)

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        info=self.get_full_name()
        if info=='':
            info=self.username
        return info

    def get_absolute_url(self):
        return reverse("User_detail", kwargs={"pk": self.pk})
 


