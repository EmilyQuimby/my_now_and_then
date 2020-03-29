from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):

    context_dict = {}

    return render(request, 'nowandthen/index.html', context=context_dict)
