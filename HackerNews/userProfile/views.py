from django.core.paginator import Paginator
from django.shortcuts import render, redirect

# Create your views here.
from authentication.models import User
from news.Counter import Counter
from news.models import Submission, Vote, ActionType
from userProfile.forms import UserForm


def show(request, user_id):
    user_form = UserForm()
    user = User.objects.get(id=user_id)
    user.timeSinceCreation()
    return render(request, "profile.html", {"form": user_form, "userRequested": user})


def submissions(request, user_id):
    user = User.objects.get(id=user_id)
    submissions = Submission.objects.filter(author=user)

    subm_paginator = Paginator(submissions, 30)
    page_num = request.GET.get('pages')

    if page_num == None:
        pages = subm_paginator.page(1)
    else:
        pages = subm_paginator.page(page_num)

    page_index = Counter()
    page_index.count = pages.start_index()
    return render(request, "upvotedSubmissions.html", {'pages': pages, 'index': page_index})


def upvoted_submissions(request, user_id):
    if request.user.is_authenticated:
        user = User.objects.get(id=user_id)
        type = ActionType.objects.get(name="Submission")
        votes = Vote.objects.filter(user=user, type=type)
        submissions = []
        for vote in votes:
            submissions.append(vote.submission)

        subm_paginator = Paginator(submissions, 30)
        page_num = request.GET.get('pages')

        if page_num == None:
            pages = subm_paginator.page(1)
        else:
            pages = subm_paginator.page(page_num)

        page_index = Counter()
        page_index.count = pages.start_index()
        return render(request, "upvotedSubmissions.html", {'pages': pages, 'index': page_index})

    else:
        return redirect("Login")


def upvoted_comments(request, user_id):
    if request.user.is_authenticated:
        user = User.objects.get(id=user_id)
        type = ActionType.objects.get(name="Comment")
        votes = Vote.objects.filter(user=user, type=type)
        comments = []
        for vote in votes:
            comments.append(vote.comment)

        return render(request, "upvotedComments.html", {"Comments": comments})

    else:
        return redirect("Login")
