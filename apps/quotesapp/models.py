# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
from  datetime import *
import bcrypt
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
password_regex = re.compile('^(?=\S{6,20}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[^A-Za-z\s0-9])')
class RegManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData["name"]) < 3:
            errors["name"] = "Name should be more than 3 characters"
        if len(postData["alias"]) < 3:
            errors["alas"] = "Alias should be more than 3 characters"
        if len(postData["email"]) < 1:
            errors["email"] = "Email field cannot be empty"
        elif not email_regex.match(postData["email"]):  
            errors["email"] = "Invalid email address"
        if len(postData["password"]) < 8:     
            errors["password"] = "Password should be more thatn 8 characters"
        count = User.objects.filter(email=postData["email"]).count()
        print count
        if count > 0:
            errors["email"] = "Email already exists"
        # elif not password_regex.match(postData["password"]):  
        #     errors["password"] = "Invalid password"
        if postData["password"] != postData["confirm"]:
            errors["confirm"] = "Password confirmation does not match"
        if len(postData["birthday"]) < 1:
            errors["birthday"] = "Birthday field cannot be empty"
        if postData["birthday"] > datetime.now().strftime("%Y-%m-%d"):
            errors["birthday"] = "Birthday can not be in the future"   
        return errors
    def login_validator(self, postData):
        errors = {}
        if len(postData["email"]) < 1:
            errors["email"] = "Email field cannot be empty"
        elif not email_regex.match(postData["email"]):  
            errors["email"] = "Invalid email address"
        if len(postData["password"]) < 8:
            errors["password"] = "Password must be longer than 8 characters"

        check = User.objects.filter(email=postData["email"])
        if len(check) == 0:
            errors["password"] = "You must enter a password"
            return errors
        if not bcrypt.checkpw(postData["password"].encode(), check[0].password.encode()):
            errors["password"] = "Password doesn't match"
        return errors
    def add_validator(self, postData):
        errors = {}
        if len(postData["quotedBy"]) < 3:
            errors["quotedBy"] = "Quoted by field must contain more than 3 characters"
        if len(postData["quotes"]) < 10:
            errors["quotes"] = "Message field must contain more than 10 characters"
        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255, )
    birthday = models.DateField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = RegManager()

class Quote(models.Model):
    quotes = models.CharField(max_length=255)
    quotedBy = models.CharField(max_length=255)
    creator = models.ForeignKey(User, related_name = "quotes")
    favusers = models.ManyToManyField(User, related_name = "favquotes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = RegManager()