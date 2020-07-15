# Generated by Django 3.0.7 on 2020-07-13 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20200713_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_id', models.CharField(max_length=50, verbose_name='Id')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('type', models.CharField(max_length=30, verbose_name='Mimetype')),
                ('imageurl', models.URLField(verbose_name='Url')),
            ],
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]