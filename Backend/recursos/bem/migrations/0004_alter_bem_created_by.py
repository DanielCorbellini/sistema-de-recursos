# Generated by Django 5.1 on 2024-10-10 00:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bem', '0003_rename_id_status_bem_bem_status_bem_alter_bem_id_bem'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='bem',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bem', to=settings.AUTH_USER_MODEL),
        ),
    ]