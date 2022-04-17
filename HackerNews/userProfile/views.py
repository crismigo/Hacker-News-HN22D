from django.shortcuts import render, redirect

# Create your views here.
from authentication.models import User
from userProfile.forms import UserForm


def show(request, user_id):
    if request.user.is_authenticated:
        user_form = UserForm()
        user = User.objects.get(id=user_id)
        user.timeSinceCreation()
        return render(request, "profile.html", {"form": user_form, "user": user})

    else:
        return redirect("/login")


def submissions(request, user_id):
    pass


def upvoted_submissions(request):
    pass


def upvoted_comments(request):
    pass
