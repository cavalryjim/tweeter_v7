# Generated by Django 3.0.3 on 2020-02-21 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['-created_at']},
        ),
    ]
