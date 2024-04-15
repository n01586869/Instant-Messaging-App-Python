# Generated by Django 5.0.4 on 2024-04-13 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='full_name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
