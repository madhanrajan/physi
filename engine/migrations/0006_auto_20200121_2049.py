# Generated by Django 2.2.8 on 2020-01-21 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0005_tag_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='tags',
        ),
        migrations.AddField(
            model_name='tag',
            name='tags',
            field=models.ManyToManyField(related_name='topics', to='engine.Topic'),
        ),
    ]
