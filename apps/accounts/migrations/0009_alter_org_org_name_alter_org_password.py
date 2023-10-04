# Generated by Django 4.2.4 on 2023-10-04 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_org_email_remove_org_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='org',
            name='org_name',
            field=models.CharField(default='UN-NAMED-ORG', error_messages={'Error': 'Orginization with this name already exists'}, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='org',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
