# Generated by Django 4.2.16 on 2024-11-05 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('identity', '0002_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, help_text='Optional', max_length=254, null=True),
        ),
        migrations.AddConstraint(
            model_name='customuser',
            constraint=models.UniqueConstraint(condition=models.Q(('email__isnull', False)), fields=('email',), name='unique_email_when_not_null'),
        ),
    ]