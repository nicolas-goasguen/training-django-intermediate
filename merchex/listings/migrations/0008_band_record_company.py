# Generated by Django 5.1.2 on 2024-10-19 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_remove_band_like_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='record_company',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
