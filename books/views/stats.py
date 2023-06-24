import datetime
import bisect
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from books.models import Book, Person

def about(request: HttpRequest) -> HttpResponse:
    '''About us page containing info about the website and the team.'''
    people = [
        ('Мікіта', 'images/member-mikita.jpg'),
        ('Яўген', 'images/member-jauhen.jpg'),
        ('Павал', 'images/member-paval.jpg'),
        ('Алесь', 'images/member-ales.jpg'),
        # ('Наста', 'images/member-nasta.jpg'),
        ('Алёна', 'images/member-alena.jpg'),
        ('Юры', 'images/member-jura.jpg'),
        ('Андрэй', 'images/member-andrey.jpg'),
        ('Вікторыя', 'images/member-andrey.jpg'),
        ('Жэня', 'images/member-andrey.jpg'),
    ]
    context = {
        'team_members': people,
        'books_count': Book.objects.count(),
    }
    return render(request, 'books/about.html', context)

def birthdays(request: HttpRequest) -> HttpResponse:
    '''Birthday page'''
    now = datetime.datetime.now()
    people = list(
        Person.objects.filter(date_of_birth__isnull=False).order_by(
            'date_of_birth__month', 'date_of_birth__day'))
    days = [p.date_of_birth.month * 31 + p.date_of_birth.day for p in people]
    ind = bisect.bisect_left(days, now.month * 31 + now.day)
    people = people[ind:] + people[:ind]

    people_with_info = []
    for person in people[:30]:
        next_birthday = datetime.date(now.year, person.date_of_birth.month,
                                      person.date_of_birth.day)
        if next_birthday < now.date():
            next_birthday = datetime.date(now.year + 1,
                                          person.date_of_birth.month,
                                          person.date_of_birth.day)
        people_with_info.append({
            'date_of_birth':
            person.date_of_birth,
            'person':
            person,
            'age':
            now.year - person.date_of_birth.year,
            'days_left': (next_birthday - now.date()).days,
            'stats':
            '%d - %d - %d' % (
                person.books_authored.count(),
                person.books_translated.count(),
                person.narrations.count(),
            ),
        })
    context = {
        'people_with_info': people_with_info,
    }
    return render(request, 'books/stats/birthdays.html', context)