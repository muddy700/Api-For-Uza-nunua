# Generated by Django 3.1.5 on 2021-01-04 23:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product_api', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('description', models.TextField(blank=True)),
                ('active', models.BooleanField(default=True)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('image1', models.ImageField(upload_to='product_pics')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_api.categories')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_api.location')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
