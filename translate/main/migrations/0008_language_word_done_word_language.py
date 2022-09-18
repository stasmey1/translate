# Generated by Django 4.1 on 2022-09-15 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_word_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='word',
            name='done',
            field=models.BooleanField(default=False, verbose_name='Изучено'),
        ),
        migrations.AddField(
            model_name='word',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='words', to='main.language', verbose_name='Язык'),
        ),
    ]
