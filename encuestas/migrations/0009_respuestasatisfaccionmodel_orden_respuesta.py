# Generated by Django 3.2.3 on 2022-05-10 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0008_auto_20220509_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='respuestasatisfaccionmodel',
            name='orden_respuesta',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]