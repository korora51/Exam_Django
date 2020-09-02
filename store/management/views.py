from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')

def contact(request):
    return render(request, 'pages/contact.html')

def normal(request):
    return render(request, 'pages/normal.html')

def faq(request):
    return render(request, 'pages/faq.html')

def forgetpass(request):
    return render(request, 'pages/forgetpass.html')

def legal_notice(request):
    return render(request, 'pages/legal_notice.html')

def login(request):
    return render(request, 'pages/login.html')

def register(request):
    return render(request, 'pages/register.html')

def special_offer(request):
    return render(request, 'pages/special_offer.html')

def store_details(request):
    return render(request, 'pages/store-details.html')
