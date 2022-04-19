from django import template
from django.shortcuts import render
from django.utils.functional import SimpleLazyObject

from item.views import view
from news.models import Vote, Comment

register = template.Library()


def isVoted(submission, user):
    try:
        voted = Vote.objects.filter(submission=submission, user=user).exists()
        return voted
    except:
        return False


register.filter('isVoted', isVoted)


def commentIsVoted(comment, user):
    try:
        voted = Vote.objects.filter(comment=comment, user=user).exists()
        return voted
    except:
        return False


register.filter('commentIsVoted', commentIsVoted)


@register.inclusion_tag('commentTemplate.html')
def commentsTree(comment_param):
    comments = Comment.objects.filter(submission_id=comment_param.id)

    return {'comments': comments}


@register.inclusion_tag('commentTemplate.html')
def commentsTreeComments(comment_param):
    comments = Comment.objects.filter(replied_comment=comment_param.id)

    return {'comments': comments}


register.filter('commentsTree', commentsTree)
register.filter('commentsTreeComments', commentsTreeComments)
