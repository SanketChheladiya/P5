# Generated by Django 3.2.8 on 2021-10-28 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_rename_postuid_post_postusername'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='postname',
            field=models.CharField(max_length=200),
        ),
    ]
