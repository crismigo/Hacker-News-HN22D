from urllib import request

from django import template
from django.shortcuts import render

from news.models import Vote

register = template.Library()



