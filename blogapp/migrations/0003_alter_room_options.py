# Generated by Django 5.1 on 2024-08-14 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_topic_room_host_message_room_topic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-updated', '-created']},
        ),
    ]
