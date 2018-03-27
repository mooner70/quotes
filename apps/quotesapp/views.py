# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *
import bcrypt
def index(request):
    return render(request, 'index.html')
def user_registration(request):
    errors = UserRegistration.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect("/")
    else:
        pwCheck = request.POST["password"]
        hash1 = bcrypt.hashpw(pwCheck.encode(), bcrypt.gensalt())
        regUser = UserRegistration.objects.create(name=request.POST["name"], alias=request.POST["alias"], email=request.POST["email"], birthday=request.POST["birthday"], password=hash1)
        request.session["user_id"] = regUser.id
        request.session['name'] = request.POST["name"]
        return redirect("/quotes")
def login(request):
    errors = UserRegistration.objects.login_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect("/")
    else:
        loginUser = UserRegistration.objects.get(email = request.POST["email"])
        request.session['name'] = loginUser.name
        request.session["user_id"] = loginUser.id
        return redirect("/quotes")
def logout(request):
    request.session.flush()
    return redirect('/')
def add_quote(request):
    errors = UserQuote.objects.add_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect("/quotes")
    else:
        quoteAdd = UserRegistration.objects.get(name=request.session['name'])
        fav = UserRegistration.objects.get(name=request.session['name'])
        UserQuote.objects.create(quoteBy=request.POST["quoteBy"], quoteMessage=request.POST["quoteMessage"], userQuote = quoteAdd, userFav = fav)
        return redirect("/quotes")        
def quotes(request):
    c = UserRegistration.objects.get(id=request.session["user_id"])
    context = {
        "quotes" : UserQuote.objects.filter(userQuote = c),
        "name" : UserRegistration.objects.filter(name=request.session['name'])}
    return render(request, 'quotes.html', context)
def add_fav(request):
    return redirect("/quotes")








# def destination(request, id):
#     context = {
#         "travel_plans" : TravelPlans.objects.get(id=id)
#         }
#     return render(request, 'destination.html', context)
# def join(request, id):
#     userjoin = UserRegistration.objects.get(id=request.session["user_id"])
#     e = TravelPlans.objects.get(id=id)
#     userjoin.trips.add(e)  
#     return redirect('/travels')
#     # e.travelers=request.session["user_id"]