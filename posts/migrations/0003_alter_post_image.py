# Generated by Django 3.2.20 on 2023-09-01 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='../default_post_jwxvtb', upload_to='images/'),
        ),
    ]
