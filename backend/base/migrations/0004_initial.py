# Generated by Django 4.2.7 on 2023-11-03 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0003_delete_videopost'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('video_url', models.CharField(blank=True, max_length=255)),
                ('thumbnail_url', models.CharField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
