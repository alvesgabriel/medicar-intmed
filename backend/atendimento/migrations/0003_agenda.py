# Generated by Django 3.0.7 on 2020-06-20 14:55

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atendimento', '0002_medico'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField()),
                ('horarios', django.contrib.postgres.fields.ArrayField(base_field=models.TimeField(), size=None)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='atendimento.Medico')),
            ],
        ),
    ]
