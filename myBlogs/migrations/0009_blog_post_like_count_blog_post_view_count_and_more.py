# Generated by Django 5.0.1 on 2024-02-02 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBlogs', '0008_remove_blog_post_blog_cat_blog_likes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='like_count',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='blog_post',
            name='view_count',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.DeleteModel(
            name='blog_likes',
        ),
    ]
