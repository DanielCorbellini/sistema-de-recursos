# Generated by Django 5.1 on 2024-12-11 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retiradas', '0004_itensretirada_id_alter_itensretirada_id_retirada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itensretirada',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
