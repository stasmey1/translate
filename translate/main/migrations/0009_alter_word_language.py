# Generated by Django 4.1 on 2022-09-15 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_language_word_done_word_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='language',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='words', to='main.language', verbose_name='Язык'),
        ),
    ]
