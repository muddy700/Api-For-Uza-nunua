from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField(default='default-for-user.png', upload_to='profile_pics')
    phone = models.CharField(max_length=11, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) 
            img.save(self.image.path)

class Product(models.Model):
    name = models.CharField(max_length=100, blank=False)
    price = models.IntegerField(blank=False)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    date_posted = models.DateTimeField(default=timezone.now)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='product_pics')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)

        img = Image.open(self.image1.path)

        if img.height != 300 or img.width != 300:
            output_size = (300, 300)
            img.thumbnail(output_size) 
            img.save(self.image1.path)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to = 'product_pics')
 
    def __str__(self):
        return self.product.name

    def save(self, *args, **kwargs):
        super(ProductImage, self).save(*args, **kwargs)

        img = Image.open(self.images.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) 
            img.save(self.images.path)