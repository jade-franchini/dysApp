# Generated by Django 5.0 on 2023-12-21 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dys_app', '0005_delete_enfant_delete_parent_remove_userprofile_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('Parent', 'parent'), ('Enfant', 'enfant')], max_length=50),
        ),
    ]