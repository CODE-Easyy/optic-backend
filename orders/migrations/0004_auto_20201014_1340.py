# Generated by Django 3.1.2 on 2020-10-14 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20201014_0150'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-id',)},
        ),
    ]