from django.shortcuts import render,redirect


# Create your views here.
from news.models import Submission, Vote, ActionType


def vote_submission(request, id):
    Vote.objects.all().delete()
    subm = Submission.objects.get(id=id)
    subm.points += 1
    subm.save()
    act = ActionType.objects.get(name="reply")
    vote= Vote(submission=subm,user=request.user,type=act)
    vote.save()
    return redirect("/news")


def unvote_submission(request, id):
    subm = Submission.objects.get(id=id)
    subm.points -= 1
    subm.save()
    #LA linia de sota tindira que ser nomes al vot que elimino
    Vote.objects.get(submission=subm,user=request.user).delete()
    return redirect("/news")


def vote_comment(request):
    pass


def unvote_comment(request):
    pass
