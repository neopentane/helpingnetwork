# Generated by Django 2.1.7 on 2019-03-29 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evelist', '0002_eventimages'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='eventprofileImage',
            field=models.ImageField(default='default.jpg', upload_to='eventprofileImage'),
        ),
    ]
