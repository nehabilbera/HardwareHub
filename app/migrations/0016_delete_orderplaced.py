# Generated by Django 4.0.4 on 2022-05-30 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_orderdetail_invoice_id_alter_order_order_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderPlaced',
        ),
    ]
