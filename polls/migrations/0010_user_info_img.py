# Generated by Django 2.1.4 on 2019-02-24 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20190224_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_info',
            name='img',
            field=models.ImageField(default='', upload_to='img'),
        ),
    ]