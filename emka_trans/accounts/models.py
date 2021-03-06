from django.db import models
from django.contrib.auth.models import User
from admin_app.models import Truck

# Create your models here.
class UserProfileInfo(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE)

	#additional classes
	#client_id
	company_name = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=12, blank=True)
	#location = models.CharField(max_length=100)
	longitude=models.FloatField(default=0)
	latitude = models.FloatField(default=0)
	profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
	is_client = models.BooleanField()
	id_cluster=models.ForeignKey(Truck,on_delete=models.CASCADE,default=0,null=True)

	def __str__(self):
		return self.user.username

	