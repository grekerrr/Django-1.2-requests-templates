import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    with open('data-398-2018-08-30.csv', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        stations_list = list()

        for row in reader:
            station = {'Name': row['Name'],
                       'Street': row['Street'],
                       'District': row['District']}
            stations_list.append(station)

    page_number = request.GET.get('page', 1)
    paginator = Paginator(stations_list, 10)
    page = paginator.get_page(page_number)
    content = page.object_list

    context = {'bus_stations': content,
               'page': page}

    return render(request, 'stations/index.html', context)
