# Generated by Django 3.2.6 on 2023-07-26 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20230725_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedimage',
            name='Age',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='uploadedimage',
            name='Gender',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='uploadedimage',
            name='Name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
