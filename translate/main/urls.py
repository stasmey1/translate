from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('list_update_words/', list_update_words, name='list_update_words'),
    path('list_word_not_done/', list_word_not_done, name='list_word_not_done'),

    path('update_word/<int:pk>/', update_word, name='update_word'),
    path('delete_word/<int:pk>/', delete_word, name='delete_word'),
]
