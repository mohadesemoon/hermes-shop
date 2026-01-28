from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=225)
    slug = models.SlugField(max_length=225, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    name = models.CharField(max_length=225)
    descriptions = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/')
    price = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('home:product_detail', args=[self.slug,])










