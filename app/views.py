import hashlib
import urllib

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import *
from django.contrib.auth import logout
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.

class IndexView(ListView):
    model = Complaint
    context_object_name = 'complaints'
    template_name = 'app/index.html'
    ordering = '-id'

    def post(self, request):
        complaint = request.POST.get('complaint') or None
        if complaint is None or not request.user.is_authenticated:
            pass
        else:
            com = Complaint(user=request.user, text=complaint)
            com.save()
            complaint = Complaint.objects.all().order_by('id').reverse()
            context = {
                "complaints": complaint
            }
        return render(request, 'app/index.html', context)


def delete(request):
    id = request.GET.get("id") or None

    if id is not None:
        com = Complaint.objects.filter(pk=id)
        if com is not None:
            complaint = com.first()
            if complaint.user == request.user or request.user.is_staff:
                complaint.delete()

    return redirect('index')


def single(request, pk):
    if request.method == "POST":
        com = get_object_or_404(Complaint, pk=pk)
        text = request.POST.get("comment") or None
        comment = Comment(commenter=request.user, complaint=com, comment=text)
        comment.save()

    context = {
        'com': get_object_or_404(Complaint, pk=pk)
    }

    return render(request, 'app/singlepost.html', context)


def logout_user(request):
    logout(request)
    return redirect('index')