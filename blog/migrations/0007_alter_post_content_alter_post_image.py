# Generated by Django 4.0.2 on 2022-02-14 00:57

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='Image',
            field=models.ImageField(default='image', upload_to=''),
        ),
    ]