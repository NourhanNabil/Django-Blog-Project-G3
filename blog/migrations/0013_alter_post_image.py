# Generated by Django 4.0.2 on 2022-02-15 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
