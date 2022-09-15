# Generated by Django 3.1.2 on 2021-03-15 06:17

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=20)),
                ('item_quantity', models.CharField(max_length=5)),
                ('item_status', models.CharField(max_length=20)),
                ('Date', models.DateField(null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='itemlist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AddItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=20)),
                ('item_quantity', models.CharField(choices=[('100gm', '100gm'), ('250gm', '250gm'), ('500gm', '500gm'), ('750gm', '750gm'), ('1kg', '1kg'), ('2kg', '2kg'), ('3kg', '3kg'), ('4kg', '4kg'), ('5kg', '5kg')], max_length=5)),
                ('item_status', models.CharField(choices=[('PENDING', 'pending'), ('BOUGHT', 'bought'), ('NOT AVAILABLE', 'not available')], default='PENDING', max_length=20)),
                ('Date', models.DateField(default=datetime.date.today)),
                ('itemlist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GBR.itemlist')),
            ],
        ),
    ]
