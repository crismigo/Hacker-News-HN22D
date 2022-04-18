from django.shortcuts import redirect


# Create your views here.
from news.models import Submission, Vote, ActionType


def vote_submission(request, id):
    if request.user.is_authenticated:
        subm = Submission.objects.get(id=id)
        act = ActionType.objects.get(name="Submission")
        vote = Vote.objects.get_or_create(submission=subm,user=request.user,type=act)
        return redirect("/news")
    else:
        return redirect("/login")


def unvote_submission(request, id):
    subm = Submission.objects.get(id=id)
    #LA linia de sota tindira que ser nomes al vot que elimino
    Vote.objects.get(submission=subm,user=request.user).delete()
    return redirect("/news")


def vote_comment(request):
    pass


def unvote_comment(request):
    pass
