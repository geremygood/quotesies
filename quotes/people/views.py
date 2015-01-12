from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404, render

from people.models import Person, Quote

def index(request):
    quote = Quote.objects.order_by('?')[0]
    person = get_object_or_404(Person, pk=quote.person.id)
    context = {
        'quote': quote,
        'person': person,
        }
    return render(request, 'people/quote_detail.html', context)

def quotes_list(request):
    latest_quotes_list = Quote.objects.order_by('-pub_date')[:50]
    context = {'latest_quotes_list': latest_quotes_list}
    return render(request, 'people/index.html', context)

def person_detail(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    quotes = get_list_or_404(Quote, person=person)
    return render(request, 'people/detail.html', {
        'person': person,
        'quotes': quotes,
        })

def quote_detail(request, person_id, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)
    person = get_object_or_404(Person, pk=person_id)
    return render(request, 'people/quote_detail.html', {
        'person': person,
        'quote': quote,
        })

def person_quotes(request, person_id):
    response = "You're looking at the quotes from person %s."
    return HttpResponse(response % person_id)

