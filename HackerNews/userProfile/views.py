from django.shortcuts import render, redirect

# Create your views here.
from authentication.models import User
from news.models import Submission
from userProfile.forms import UserForm


def show(request, user_id):
    if request.user.is_authenticated:
        user_form = UserForm()
        user = User.objects.get(id=user_id)
        user.timeSinceCreation()
        return render(request, "profile.html", {"form": user_form, "user": user})

    else:
        return redirect("Login")


def submissions(request, user_id):
    if request.user.is_authenticated:
        user_form = UserForm()
        user = User.objects.get(id=user_id)
        submissions = Submission.objects.filter(author=user)

        for subm in submissions:
            subm.timesincecreation()
            subm.domainurl()
        return render(request, "userSubmissions.html", {"form": user_form, "user": user})

    else:
        return redirect("Login")


def upvoted_submissions(request, user_id):
    pass


def upvoted_comments(request, user_id):
    pass
