# Generated by Django 3.2 on 2024-01-10 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_category_thumb'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='home_article',
            field=models.BooleanField(default=False),
        ),
    ]
