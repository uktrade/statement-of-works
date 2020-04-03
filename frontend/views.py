from django.shortcuts import render

def index(request):
    """Endpoint for index view."""
    return render(request, 'frontend/index.html')
