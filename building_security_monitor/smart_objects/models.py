from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _
class AbstractDevice(models.Model):
	"""Model definition for AbstractDevice."""

	device_model = models.CharField(_('Model'), max_length=50)
	manufacture = models.CharField(_('Manufacture'), max_length=50)
	created_date = models.DateField(_('Build date'), auto_now_add=True)
	warranty_date = models.DateField(_('Warranty exp date'), auto_now=False, auto_now_add=False)
	has_warranty = models.BooleanField()
	device_uuid = models.UUIDField(uniqe=True,primary_key=True,default=uuid.uuid4,editable=False)
	ip_addr = models.GenericIPAddressField(_('Ip address'), protocol='both', unpack_ipv4=False)
	class Meta:
		"""Meta definition for AbstractDevice."""
		abstract=True
		verbose_name = 'AbstractDevice'
		verbose_name_plural = 'AbstractDevices'

	def __str__(self):
		"""Unicode representation of AbstractDevice."""
		pass

# Create your models here.
class Lock(AbstractDevice):
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
class CCTV(AbstractDevice):
	"""Model definition for CCTV."""

	# TODO: Define fields here

	class Meta:
		"""Meta definition for CCTV."""

		verbose_name = 'CCTV'
		verbose_name_plural = 'CCTVs'

	def __str__(self):
		"""Unicode representation of CCTV."""
		pass
