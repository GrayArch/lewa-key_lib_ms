# Generated by Django 4.1.9 on 2023-06-28 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_publisher'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name_plural': 'Categories'},
        ),
    ]