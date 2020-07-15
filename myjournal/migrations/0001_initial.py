# Generated by Django 3.0.7 on 2020-07-15 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('date', models.DateField(verbose_name='Date')),
                ('journalurl', models.URLField(blank=True, verbose_name='Url')),
                ('journal', models.TextField(blank=True, verbose_name='Journal')),
                ('journaldoc', models.FileField(blank=True, null=True, upload_to='Thumbnails/journals/')),
            ],
        ),
    ]
