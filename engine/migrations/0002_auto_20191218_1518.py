# Generated by Django 2.2.8 on 2019-12-18 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='topic',
            name='description',
        ),
        migrations.AddField(
            model_name='topic',
            name='tags',
            field=models.ManyToManyField(to='engine.Tag'),
        ),
    ]
