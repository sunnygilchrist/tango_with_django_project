from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to Rango! <a href=\"/rango/about/\">Find out more about Rango here.</a>")

def about(request):
    return HttpResponse("Welcome to Rango's about page! <a href=\"/rango/\">Go home.</a>")