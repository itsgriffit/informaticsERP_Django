# Generated by Django 3.1 on 2021-12-08 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='descriptioin',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='product',
            name='expire_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='package_form',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
