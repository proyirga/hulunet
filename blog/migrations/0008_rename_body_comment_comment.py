# Generated by Django 4.2.4 on 2023-09-09 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_comment_delete_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='comment',
        ),
    ]
