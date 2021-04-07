from django.db import models
from django.contrib.auth.models import AbstractUser,EmptyManager,Group,Permission
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from account.models import User

# Create your models here.
# class AbstractPerson(AbstractUser):
#     """Model definition for Person."""
#     GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#         )
#     ROLE_CHOICES = (
#         ('S', 'Son'),
#         ('D', 'Daughter'),
#         )
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
#     birth_date=models.DateField(_("Date of birth"),)
#     role=models.CharField(_("Role in family"),max_length=1, choices=ROLE_CHOICES)
#     is_staff = True
#     is_superuser=False

#     groups = None

#     user_permissions = models.ManyToManyField(
#         Permission,
#         verbose_name=_('user permissions'),
#         blank=True,
#         help_text=_('Specific permissions for this user.'),
#         related_name="%(class)s_related",
#         related_query_name="%(class)ss",
#     )
    

#     class Meta:
#         """Meta definition for Person."""
#         abstract=True
#         verbose_name = 'Person'
#         verbose_name_plural = 'Persons'


class Person(User):
    """Model definition for Person."""
    class Meta:
        """Meta definition for Person."""

        verbose_name = 'Person'
        verbose_name_plural = 'Persons'

    def __str__(self):
        """Unicode representation of Person."""
        info=self.get_full_name()
        if info=='':
            info=self.username
        return info


class Father(User):
    """Model definition for Father."""
    def __init__(self, *args, **kwargs):
        kwargs['role'] = 'F'
        super().__init__(*args, **kwargs)
    
    

    class Meta:
        """Meta definition for Father."""

        verbose_name = 'Father'
        verbose_name_plural = 'Fathers'

    # def __str__(self):
    #     """Unicode representation of Father."""
    #     return self.get_full_name()


class Mother(User):
    """Model definition for Father."""
    def __init__(self, *args, **kwargs):
        kwargs['role'] = 'M'
        kwargs['gender'] = 'F'
        super().__init__(*args, **kwargs)
    

    class Meta:
        """Meta definition for Mother."""

        verbose_name = 'Mother'
        verbose_name_plural = 'Mothers'

    def __str__(self):
        """Unicode representation of Mother."""
        return self.get_full_name()



class Family(models.Model):
    """Model definition for Family."""
    father=models.OneToOneField(Father, verbose_name=_("father"),related_name='f_family', on_delete=models.CASCADE)
    mother=models.OneToOneField(Mother, verbose_name=_("mother"),related_name='m_family', on_delete=models.CASCADE)
    # members=models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("members"),related_name='p_family', null=True,on_delete=models.SET_NULL)
    
    class Meta:
        """Meta definition for Family."""

        verbose_name = 'Family'
        verbose_name_plural = 'Familys'

    def __str__(self):
        """Unicode representation of Family."""
        father_name=self.father.first_name
        ftaher_lanme=self.father.last_name
        mother_name=self.mother.first_name
        return 'family of %s %s %s' %(father_name,mother_name,ftaher_lanme)
