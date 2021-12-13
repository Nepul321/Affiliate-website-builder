from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(unique=True)
    key = models.CharField(max_length=100000000000000000000000000000000000000000000000000000)
    purchased = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name', 'key', 'purchased']

class Product(models.Model):
    name = models.CharField(max_length=1000)
    link = models.URLField()
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='products/')

    def __str__(self):
        return "Product " + str(self.id)

class Website(models.Model):
    name = models.CharField(max_length=255, unique=True)
    # header_title = models.CharField(max_length=255, default='')
    # header_text = models.TextField(default='')
    image1 = models.ImageField(upload_to='carousel/', default='')
    image2 = models.ImageField(upload_to='carousel/', default='')
    image3 = models.ImageField(upload_to='carousel/', default='')
    products = models.ManyToManyField(Product, related_name="website_products", blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name