# Generated by Django 4.2.7 on 2023-11-13 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylittlenigga', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(default='default'),
            preserve_default=False,
        ),
    ]
