# Generated by Django 3.2.8 on 2021-10-23 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('door', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='user/photo/none_user.png', null=True, upload_to='user/photo/', verbose_name='Фото пользователя'),
        ),
    ]
