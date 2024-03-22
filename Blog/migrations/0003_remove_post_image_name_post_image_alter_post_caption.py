# Generated by Django 5.0 on 2024-01-21 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_rename_excerpt_post_excerpt_alter_post_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_name',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='posts'),
        ),
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.ManyToManyField(to='Blog.tag', verbose_name='Tag'),
        ),
    ]