# Generated by Django 4.1.5 on 2023-03-14 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['is_read', '-created']},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['created']},
        ),
    ]
