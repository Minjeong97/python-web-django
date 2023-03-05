from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def hihihi(request):
    import random
    numbers = random.sample(range(1, 46), 6)
    return HttpResponse(numbers)

def hello_world(request):
    pass

