from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Working here ...')

def details(request, question_id):
    return HttpResponse('Checking question %s' % question_id)

def results(request, question_id):
    response = 'You are looking at the results for question %s'
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse('You are voting on question %s' % question_id)
