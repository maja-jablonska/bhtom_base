# Generated by Django 4.0.4 on 2023-10-25 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bhtom_dataproducts', '0002_alter_reduceddatum_data_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ccdphotjob',
            name='instrument',
            field=models.CharField(blank=True, help_text='instrument identification (not used by ccdphot)', max_length=100),
        ),
    ]