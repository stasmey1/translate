from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Word
import string


class WordForm(ModelForm):
    class Meta:
        model = Word
        fields = ('ru', 'en', 'level', 'type', 'done')

    def clean(self):
        super().clean()

        ru = self.cleaned_data['ru']
        if any([i.lower() not in ''.join([chr(i) for i in range(ord('а'), ord('я') + 1)]) for i in ru]):
            self.errors['ru'] = ValidationError('только кирилица')

        en = self.cleaned_data['en']
        if any([i not in string.ascii_letters for i in en]):
            self.errors['en'] = ValidationError('только латиница')
