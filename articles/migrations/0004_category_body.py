# Generated by Django 3.2 on 2023-12-29 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_category_tour'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='body',
            field=models.TextField(blank=True),
        ),
    ]
