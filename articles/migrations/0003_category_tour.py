# Generated by Django 3.2 on 2023-12-29 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_thumb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=1000, unique=True)),
                ('slug', models.SlugField(max_length=1000, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('place', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('thumb', models.ImageField(default='default.png', upload_to='')),
                ('pax1', models.PositiveIntegerField(blank=True)),
                ('pax2', models.PositiveIntegerField(blank=True)),
                ('pax3', models.PositiveIntegerField(blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_special', models.BooleanField(default=False)),
                ('home_tour', models.BooleanField(default=False)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.category')),
            ],
        ),
    ]
