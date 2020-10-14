# Generated by Django 3.1.2 on 2020-10-13 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0006_auto_20201011_0142'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('products', models.ManyToManyField(to='orders.OrderItem')),
            ],
        ),
    ]