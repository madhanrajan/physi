# Generated by Django 2.2.8 on 2020-03-25 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0009_unsafetag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='document',
            field=models.FileField(blank=True, upload_to='book/%Y/%m/%d'),
        ),
    ]