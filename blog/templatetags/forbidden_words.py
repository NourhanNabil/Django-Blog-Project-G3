from blog.models import ForbiddenWord
from django import template


def forbid(content: str):
    for word in ForbiddenWord.objects.values_list("forbidden_word"):
        word = word[0]
        replace_with = "*" * len(word)
        content = content.replace(word, replace_with)
        content = content.replace(word.lower(), replace_with)
        content = content.replace(word.upper(), replace_with)
        content = content.replace(word.capitalize(), replace_with)
    return content


register = template.Library()

register.filter("forbid", forbid)
