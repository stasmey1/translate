# Generated by Django 4.1 on 2022-09-14 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='level',
            field=models.CharField(choices=[(1, 'easy'), (2, 'medium'), (1, 'hard')], default=1, max_length=10),
        ),
        migrations.AlterField(
            model_name='word',
            name='type',
            field=models.CharField(choices=[(6, 'другое'), (5, 'местоимение'), (3, 'прилагательное'), (4, 'наречие'), (2, 'существительное'), (1, 'глагол')], default=1, max_length=10),
        ),
        migrations.DeleteModel(
            name='Level',
        ),
        migrations.DeleteModel(
            name='Type',
        ),
    ]