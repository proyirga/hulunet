from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from PIL import Image

class Item4Rent(models.Model):
    item_name = models.CharField(max_length=100)
    image = models.ImageField(default=None, blank=True, null=True, upload_to='rents-img')
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    contact = models.CharField(max_length=25)
    cost = models.IntegerField(default=000)
    rented = models.BooleanField(default=False)


    def get_absolute_url(self):
        return reverse('item-detail', kwargs={'pk':self.pk})
    

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)