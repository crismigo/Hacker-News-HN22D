from django import template
from django.shortcuts import render

from item.views import view
from news.models import Vote, Comment

register = template.Library()


def isVoted(submission, user):
    voted = Vote.objects.filter(submission=submission, user=user).exists()
    return voted


register.filter('isVoted', isVoted)


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