# Generated by Django 4.2.5 on 2024-02-21 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_options_remove_comment_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='body',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
    ]