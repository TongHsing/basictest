from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    context = {
    'num_books': 1,
    'num_instances': 2,
    'num_instances_available': 3,
    'num_authors': 4,
    }

    return render(request, 'index.html', context=context)
