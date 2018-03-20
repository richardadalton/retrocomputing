from django.shortcuts import render

# Create your views here.
def home(request):
    """A view that displays the index page"""
    return render(request, "home/index.html")
