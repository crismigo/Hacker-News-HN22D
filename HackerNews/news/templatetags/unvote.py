from django import template

from news.models import Vote, Comment, Submission

register = template.Library()


def get_num_comments_from_comments(comment):
    comments = Comment.objects.filter(replied_comment=comment)
    count = 0
    for comm in comments:
        count = count + 1 + get_num_comments_from_comments(comm)
    return count


def get_num_comments(id):
    count = 0
    subm = Comment.objects.filter(submission_id=id)
    for comment in subm:
        count = count + 1 + get_num_comments_from_comments(comment)
    return count


register.filter('get_num_comments', get_num_comments)


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


def timeFromVotes(comment):
    if comment.type.name == "Submission":
        subm = Submission.objects.get(id=comment.submission.id)
        return subm.timesincecreation()
    else:
        return timeFromVotes(comment.replied_comment)


register.filter('timeFromVotes', timeFromVotes)


def titleFromVotes(comment):
    if comment.type.name == "Submission":
        subm = Submission.objects.get(id=comment.submission.id)
        return subm.title
    else:
        return timeFromVotes(comment.replied_comment)


register.filter('titleFromVotes', titleFromVotes)


def idFromVotes(comment):
    if comment.type.name == "Submission":
        subm = Submission.objects.get(id=comment.submission.id)
        return subm.id
    else:
        return timeFromVotes(comment.replied_comment)


register.filter('idFromVotes', idFromVotes)


@register.inclusion_tag('commentTemplate.html')
def commentsTree(comment_param, user):
    comments = Comment.objects.filter(submission_id=comment_param.id)

    return {'comments': comments, "user": user}


@register.inclusion_tag('commentTemplate.html')
def commentsTreeComments(comment_param, user):
    comments = Comment.objects.filter(replied_comment=comment_param.id)

    return {'comments': comments, "user": user}


register.filter('commentsTree', commentsTree)
register.filter('commentsTreeComments', commentsTreeComments)
