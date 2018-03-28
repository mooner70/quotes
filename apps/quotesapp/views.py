# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *
import bcrypt
def index(request):
    return render(request, 'index.html')
def user_registration(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect("/")
    else:
        pwCheck = request.POST["password"]
        hash1 = bcrypt.hashpw(pwCheck.encode(), bcrypt.gensalt())
        regUser = User.objects.create(name=request.POST["name"], alias=request.POST["alias"], email=request.POST["email"], birthday=request.POST["birthday"], password=hash1)
        request.session["user_id"] = regUser.id
        request.session['name'] = request.POST["name"]
        return redirect("/quotes")
def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect("/")
    else:
        loginUser = User.objects.get(email = request.POST["email"])
        request.session['name'] = loginUser.name
        request.session["user_id"] = loginUser.id
        return redirect("/quotes")
def logout(request):
    request.session.flush()
    return redirect('/')
def add_fav(request):
    errors = Quote.objects.add_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect("/quotes")
    else:
        Quote.objects.create(quotedBy=request.POST["quotedBy"], quotes=request.POST["quotes"], creator=User.objects.get(id=request.session["user_id"]))
        return redirect("/quotes") 
def quotes(request):
    user = User.objects.get(id=request.session["user_id"])
    context = {
        "quotes" : Quote.objects.exclude(favusers=user),
        "favquotes" : Quote.objects.filter(favusers=user)
        }
    return render(request, 'quotes.html', context)
def user_quotes(request, id):
    context = {
        "userQuotes" : Quote.objects.filter(creator=User.objects.get(id=id)),
        "count" : Quote.objects.filter(creator=User.objects.get(id=id)).count(),
        "creator" : User.objects.get(id=id),
        }
    return render(request, 'userQuotes.html', context)
def add_to_favorite(request, id):
    this_user = User.objects.get(id=request.session["user_id"])
    this_quote = Quote.objects.get(id=id)
    this_quote.favusers.add(this_user)
    return redirect('/quotes')
def remove_from_favorite(request, id):
    this_user = User.objects.get(id=request.session["user_id"])
    this_quote = Quote.objects.get(id=id)
    this_quote.favusers.remove(this_user)
    return redirect('/quotes')
