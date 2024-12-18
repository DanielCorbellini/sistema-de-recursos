# Generated by Django 5.1 on 2024-10-31 00:24

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoBem',
            fields=[
                ('id_tipo_bem', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_bem', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tipo_bem',
            },
        ),
        migrations.CreateModel(
            name='Bem',
            fields=[
                ('id_bem', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('descricao', models.TextField(blank=True, null=True)),
                ('permite_reserva', models.BooleanField(null=True)),
                ('status_bem', models.CharField(choices=[('R', 'Retirado'), ('D', 'Disponível')], default='D', max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bem', to=settings.AUTH_USER_MODEL)),
                ('id_tipo_bem', models.ForeignKey(db_column='id_tipo_bem', on_delete=django.db.models.deletion.CASCADE, to='bem.tipobem')),
            ],
            options={
                'db_table': 'bem',
            },
        ),
    ]
