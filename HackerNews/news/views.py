from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from news.Counter import Counter
from news.models import Submission, SubmissionType


def news(request):
    subm_paginator = Paginator(Submission.objects.order_by('-points'), 30)
    page_num = request.GET.get('pages')

    if page_num == None:
        pages = subm_paginator.page(1)
    else:
        pages = subm_paginator.page(page_num)

    page_index = Counter()
    page_index.count = pages.start_index()
    return render(request, "news.html", {'pages': pages, 'index': page_index})


def newest(request):
    subm_paginator = Paginator(Submission.objects.order_by('-created_at'), 30)
    page_num = request.GET.get('pages')
    if page_num == None:
        pages = subm_paginator.page(1)
    else:
        pages = subm_paginator.page(page_num)
    page_index = Counter()
    page_index.count = pages.start_index()
    return render(request, "newsest.html", {"pages": pages, 'index': page_index})


def ask(request):
    type = SubmissionType.objects.get(name="ask")
    subm_paginator = Paginator(Submission.objects.filter(type=type).order_by('-points'), 30)
    page_num = request.GET.get('pages')

    if page_num == None:
        pages = subm_paginator.page(1)
    else:
        pages = subm_paginator.page(page_num)
    page_index = Counter()
    page_index.count = pages.start_index()

    return render(request, "ask.html", {"pages": pages, 'index': page_index})
