from django.shortcuts import render


def contacts(requests):
    return render(requests, 'catalog/contacts/contacts.html')


def home(requests):
    return render(requests, 'catalog/home.html')
