# Generated by Django 4.2.16 on 2024-11-06 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('identity', '0005_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'SystemUser', 'verbose_name_plural': 'SystemUsers'},
        ),
    ]
