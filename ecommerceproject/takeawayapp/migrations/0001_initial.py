# Generated by Django 3.2.3 on 2021-05-29 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='category')),
                ('cat_desc', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('category_name',),
            },
        ),
        migrations.CreateModel(
            name='Restourent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restourent_name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('tagline', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('location', models.CharField(max_length=250)),
                ('open', models.BooleanField(default=True)),
                ('restourent_image', models.ImageField(blank=True, upload_to='restourent')),
                ('opening', models.DateTimeField(blank=True)),
                ('closing', models.DateTimeField(blank=True)),
                ('working_days', models.CharField(blank=True, max_length=250)),
            ],
            options={
                'verbose_name': 'restourent',
                'verbose_name_plural': 'restourents',
                'ordering': ('restourent_name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_desc', models.TextField(blank=True)),
                ('stock', models.IntegerField()),
                ('available', models.BooleanField(default=True)),
                ('product_image', models.ImageField(blank=True, upload_to='product')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='takeawayapp.category')),
                ('restourent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='takeawayapp.restourent')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'ordering': ('product_name',),
            },
        ),
    ]