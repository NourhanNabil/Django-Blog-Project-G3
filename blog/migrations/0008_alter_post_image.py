# Generated by Django 4.0.2 on 2022-02-14 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_content_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='blog/static/img'),
        ),
    ]