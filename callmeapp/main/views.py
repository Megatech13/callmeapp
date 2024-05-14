from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    data = {
        'title': 'Ищите людей, а не сайты',
        'users': [
            {
                'name': 'Igor',
                'description': 'Знаю всё про порнотехнологии, 12 лет опыта в гей индустрии',
                'price': '100 руб/мин'
            },
            {
                'name': 'Ipolit',
                'description': 'Знаю всё про нанотехнологии, 10 лет изучаю свой пенис',
                'price': '50 руб/мин'
            },
            {
                'name': 'Mary',
                'description': 'Знаю всё про всех',
                'price': '1000 руб/мин'
            },
        ]
    }
    return render(request, 'main/index.html', data)

def specialists(request):
    return render(request,'main/about.html')

def my_contacts(request):
    return render(request, 'main/my_contacts.html')
