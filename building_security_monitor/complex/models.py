from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.contrib.auth.models import Group
from account.models import User
from family.models import Family


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
		return str(self.no)

	def get_absolute_url(self):
		return reverse("block_detail", kwargs={"pk": self.pk})


class Unit(models.Model):
	owner=models.OneToOneField(User, verbose_name=_("owner"),null=True,blank=True, on_delete=models.SET_NULL)
	owner_family=models.OneToOneField(Family, verbose_name=_("familly"),null=True,blank=True, on_delete=models.SET_NULL)
	phone=models.CharField(_("unit phone number"), max_length=11)
	block=models.ForeignKey(Block, verbose_name=_("block"), on_delete=models.CASCADE)
	no=models.IntegerField(_("unit number"))
	
	
	class Meta:
		verbose_name = _("Unit")
		verbose_name_plural = _("Units")

	def __str__(self):
		if self.owner:
			owner_full_name=self.owner.get_full_name()
			info='unit number %i , %s'%(self.no,owner_full_name)
			return info
		return 'unit number %i'%(self.no)

	def get_absolute_url(self):
		return reverse("Unit_detail", kwargs={"pk": self.pk})

class Room(models.Model):
	"""Model definition for Room."""

	unit = models.ForeignKey(Unit,null=True, on_delete=models.SET_NULL)

	class Meta:
		"""Meta definition for Room."""

		verbose_name = 'Room'
		verbose_name_plural = 'Rooms'

	def __str__(self):
		"""Unicode representation of Room."""
		pass
