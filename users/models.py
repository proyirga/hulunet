from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Bio(models.Model):
    text = models.TextField()
    title = models.CharField(max_length=50)
    date = models.DateTimeField()

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_imgs')
    bios = models.ManyToManyField(Bio, related_name='profiles')


    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)




class Broker(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    license_id = models.CharField(max_length=25)
    license = models.ImageField(upload_to='licenses')
    office_address = models.CharField(max_length=200)