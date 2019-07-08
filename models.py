from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
	#creating one to one relationship with the User model
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.png', upload_to='profile_pics')

	#creating danda str method to print the results how we want it to be printed

	def __str__(self):
		return f'{self.user.username} Profile'

#defining our save function to override the django build save function 
#save by super()
	def save(self):
		super().save()

		img = Image.open(self.image.path)

		if img.height > 250 or img.width > 250:
			output_size = (250, 250)
			img.thumbnail(output_size)
			#saving the image in the same path and overide the learger image
			img.save(self.image.path)

    
     