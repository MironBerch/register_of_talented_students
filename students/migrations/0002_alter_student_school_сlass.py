# Generated by Django 4.1.4 on 2023-02-11 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='school_сlass',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='school_сlass', to='students.class'),
        ),
    ]
