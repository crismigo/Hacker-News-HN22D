from django.core.paginator import Paginator
from django.shortcuts import render, redirect

# Create your views here.
from authentication.models import User
from news.Counter import Counter
from news.models import Submission, Vote, ActionType
from userProfile.forms import UserForm


def show(request, user_id):
    user = User()
    if request.method == "POST":
        if request.user.is_authenticated:
            user_form = UserForm(data=request.POST)
            if user_form.is_valid():
                user = User.objects.get(id=user_id)
                user.about = request.POST.get("about")
                user.email = request.POST.get("email")
                user.save()
        else:
            return redirect("Login")
    else:
        user = User.objects.get(id=user_id)
        user.timeSinceCreation()
        user_form = UserForm(instance=user)
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
    return render(request, "userSubmissions.html", {'pages': pages, 'index': page_index, "requestedUser": user})


def upvoted_submissions(request, user_id):
    if request.user.is_authenticated:
        user = User.objects.get(id=user_id)
        type = ActionType.objects.get(name="Submission")
        votes = Vote.objects.filter(user=user, type=type)
        submissions = []
        for vote in votes:
            if vote.submission.author.id != user_id:
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
        print(comments)
        subm_paginator = Paginator(comments, 30)
        page_num = request.GET.get('pages')

        if page_num == None:
            pages = subm_paginator.page(1)
        else:
            pages = subm_paginator.page(page_num)

        page_index = Counter()
        page_index.count = pages.start_index()
        return render(request, "upvotedComments.html", {'pages': pages, 'index': page_index})
    else:
        return redirect("Login")
