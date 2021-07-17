# Generated by Django 3.2.5 on 2021-07-16 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_presence_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presence',
            name='status',
            field=models.CharField(choices=[('CAN', 'Canceled'), ('INV', 'Invited'), ('INT', 'Interested'), ('CON', 'Confirmed')], default='INV', max_length=3, verbose_name=''),
        ),
    ]
