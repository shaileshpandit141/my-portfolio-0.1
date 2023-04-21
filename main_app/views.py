from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def index(request):
    temp = {'page_title': 'index'}
    return render(request, 'index.html', temp)


def home(request):
    temp = {'page_title': 'home'}
    return render(request, 'home.html', temp)


def about(request):
    temp = {'page_title': 'about'}
    return render(request, 'about.html', temp)


def services(request):
    temp = {'page_title': 'services'}
    return render(request, 'services.html', temp)


def portfolio(request):
    temp = {'page_title': 'portfolio'}
    return render(request, 'portfolio.html', temp)


def contact(request):
    contact_dit = {}
    try:
        if request.method == 'POST':
            fname = request.POST['fname']
            email = request.POST['email']
            number = request.POST['number']
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            contact_dit = {
                'page_title': 'Contact',
                'fname': fname,
                'email': email,
                'number': number,
                'subject': subject,
                'message': message,
            }
            print('------------------------------------')
            for i in contact_dit:
                print(i, ':', contact_dit[i])
            print('------------------------------------')
    except:
        pass
    return render(request, 'contact.html', contact_dit)



def test(request):
    return HttpResponse('<h1> This is test text.</h1>')
