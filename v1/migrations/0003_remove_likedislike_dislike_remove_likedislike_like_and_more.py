# Generated by Django 5.0.1 on 2024-02-02 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0002_rename_praduct_likedislike_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likedislike',
            name='dislike',
        ),
        migrations.RemoveField(
            model_name='likedislike',
            name='like',
        ),
        migrations.AddField(
            model_name='product',
            name='ld_like',
            field=models.BooleanField(default=False),
        ),
    ]
