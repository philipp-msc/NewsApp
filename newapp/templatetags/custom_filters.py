from django import template

register = template.Library()

censored_words = ['украли', 'читеров', 'Windows', 'чипов']

@register.filter()
def censor(value):
    for word in censored_words:
        value = value.replace(word, '*' * len(word))
    return value



