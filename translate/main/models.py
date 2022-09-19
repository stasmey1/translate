from django.db import models
from django.shortcuts import reverse
from django.core.exceptions import ValidationError
from django.core import validators
import string


def validate_ru(ru):
    if any([i.lower() not in ''.join([chr(i) for i in range(ord('а'), ord('я') + 1)]) for i in ru]):
        raise ValidationError(message='только кирилица', code='invalid')


def validate_en(en):
    if any([i not in string.ascii_letters for i in en]):
        raise ValidationError('только латиница')


class Language(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Word(models.Model):
    TYPE = (
        ('a', 'глагол'),
        ('b', 'существительное'),
        ('c', 'прилагательное'),
        ('d', 'наречие'),
        ('e', 'местоимение'),
        ('f', 'другое'),
    )

    LEVEL = (
        ('easy', 'легкий'),
        ('medium', 'средний'),
        ('hard', 'сложный'),
    )
    ru = models.CharField(max_length=100, validators=[validate_ru])
    en = models.CharField(max_length=100, validators=[validate_en])
    type = models.CharField(max_length=10, choices=TYPE, blank=True, null=True, verbose_name='Тип')
    level = models.CharField(max_length=10, choices=LEVEL, blank=True, null=True, verbose_name='Уровень сложности')
    time_create = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField('Изучено', default=False)
    language = models.ForeignKey(Language,
                                 on_delete=models.SET_DEFAULT,
                                 default=Language.objects.get(name='English').id,
                                 null=True, blank=True, related_name='words',
                                 verbose_name='Язык')

    def __str__(self):
        return f'{self.ru} - {self.en}'

    def get_absolute_url(self):
        return reverse('update_word', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Слово'
        verbose_name_plural = 'Слова'
        ordering = ['-time_create', ]
