from django.shortcuts import render

def home(request):
    ''' Renders the template for home page of the website '''

    return render(request, 'index.html')
