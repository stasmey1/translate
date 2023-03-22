LEVEL_COLORS = {
    'easy': 'green',
    'medium': 'yellow',
    'hard': 'red'
}


def add_color(word):
    if word.level:
        word.level_color = LEVEL_COLORS.get(word.level)
        word.save()
