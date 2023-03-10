# Generated by Django 4.1.5 on 2023-03-08 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_fbhub', '0007_alter_avatar_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='estadio',
            name='equipo',
            field=models.CharField(default='Default', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jugador',
            name='equipo_act',
            field=models.CharField(default='Default', max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='equipo',
            name='escudo',
            field=models.ImageField(default='fbhub/media/No-Image-Placeholder.jpg', upload_to='fbhub/media'),
        ),
    ]
