from django import template

from news.models import Vote

register = template.Library()


def isVoted(submission, user):
    voted = Vote.objects.filter(submission=submission, user=user).exists()
    return voted


register.filter('isVoted', isVoted)
