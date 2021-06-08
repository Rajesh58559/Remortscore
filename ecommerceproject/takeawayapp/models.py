from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    image = models.ImageField(upload_to='category', blank=True)
    cat_desc = models.TextField(blank=True)

    class Meta:
        ordering = ('category_name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('takeawayapp:products_by_category', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.category_name)


class Restourent(models.Model):
    restourent_name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    tagline = models.TextField(blank=True)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=250)
    open = models.BooleanField(default=True)
    restourent_image = models.ImageField(upload_to='restourent', blank=True)
    opening = models.DateTimeField(blank=True)
    closing = models.DateTimeField(blank=True)
    working_days = models.CharField(max_length=250, blank=True)

    class Meta:
        ordering = ('restourent_name',)
        verbose_name = 'restourent'
        verbose_name_plural = 'restourents'

    def __str__(self):
        return '{}'.format(self.restourent_name)


class Product(models.Model):
    product_name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_desc = models.TextField(blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    restourent = models.ForeignKey(Restourent, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='product', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('takeawayapp:prodDetails', args=[self.category.slug, self.slug])

    class Meta:
        ordering = ('product_name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return '{}'.format(self.product_name)
