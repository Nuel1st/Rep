from django.shortcuts import render

# Create your views here.

def home(request):
    return render( request, 'index.html')

def login(request):
    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def detail(request):
    return render(request, 'detail.html')

def service(request):
    return render(request, 'service.html')

def plan(request):
    return render(request, 'plan.html')

def faq(request):
    return render(request, 'faq.html')

# def team(request):
#     return render(request, 'team.html')


