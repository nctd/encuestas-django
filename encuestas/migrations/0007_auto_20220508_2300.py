# Generated by Django 3.2.3 on 2022-05-09 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0006_auto_20220508_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursoencuestamodel',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encuestas.cursomodel'),
        ),
        migrations.AlterField(
            model_name='cursoencuestamodel',
            name='encuesta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encuestas.encuestasatisfaccionmodel'),
        ),
    ]
