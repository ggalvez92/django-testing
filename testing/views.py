from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone


def main(request):
    # return HttpResponse("You're looking at question")
    return render(request, 'polls/main.html',)
