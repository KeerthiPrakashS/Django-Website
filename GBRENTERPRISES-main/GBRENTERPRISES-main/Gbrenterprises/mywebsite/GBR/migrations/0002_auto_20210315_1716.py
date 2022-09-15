# Generated by Django 3.1.2 on 2021-03-15 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GBR', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='additem',
            name='item_status',
        ),
        migrations.AddField(
            model_name='additem',
            name='item_gaze',
            field=models.CharField(choices=[('HEAVY', 'HEAVY'), ('LIGHT', 'LIGHT'), ('ULTRA', 'ULTRA')], default='LIGHT', max_length=20),
        ),
        migrations.AlterField(
            model_name='additem',
            name='item_name',
            field=models.CharField(choices=[('10mm sheets(3x4)', '10mm sheets(3x4)'), ('12mm sheets(3x4)', '12mm sheets(3x4)'), ('Batam', 'Batam'), ('Patti', 'Patti'), ('SPL', 'SPL'), ('Support L', 'Support L'), ('POP Bag', 'POP Bag'), ('Nails', 'Nails'), ('Fan Hook', 'Fan Hook'), ('Star Screw', 'Star Screw'), ('Anchor bolts', 'Anchor bolts')], default='10mm sheets(3x4)', max_length=20),
        ),
        migrations.AlterField(
            model_name='additem',
            name='item_quantity',
            field=models.IntegerField(default='0', max_length=5),
        ),
    ]
