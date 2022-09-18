from django.shortcuts import render, redirect, get_object_or_404
from .models import Word
from .forms import WordForm

from rest_framework import generics, viewsets
from .serializers import WordSerializer



def index(request):
    if request.GET.get('level'):
        words = Word.objects.filter(level=request.GET.get('level'))
    else:
        words = Word.objects.all()
    form = WordForm()
    template = 'main/word_list.html'

    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, template, locals())

    return render(request, template, locals())


def list_word_not_done(request):
    if request.GET.get('level') is not None:
        words = Word.objects.filter(level=request.GET.get('level'), done=False)
    else:
        words = Word.objects.filter(done=False)
    form = WordForm()
    template = 'main/word_list.html'
    return render(request, template, locals())


def list_update_words(request):
    words = Word.objects.all()
    template = 'main/list_update_words.html'
    return render(request, template, locals())


def update_word(request, pk):
    word = get_object_or_404(Word, pk=pk)

    if request.method == 'POST':
        form = WordForm(request.POST, instance=word)
        if form.is_valid():
            form.save()
            return redirect('list_update_words')

    form = WordForm(instance=word)
    template = 'main/update_word.html'
    return render(request, template, locals())


def delete_word(request, pk):
    word = get_object_or_404(Word, pk=pk)

    if request.method == 'POST':
        if request.POST.get('delete') == 'yes':
            word.delete()
        return redirect('list_update_words')

    template = 'main/delete_word.html'
    return render(request, template, locals())

class WordVeiwSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

