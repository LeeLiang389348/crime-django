from django.shortcuts import render
from django.http import HttpResponse
from .models import crime
from django.core.paginator import Paginator


def say(request):
    return HttpResponse("hello")

def render_page(request):
    return render(request, "test.html")

def list_crimes(request):
	crime_list = crime.objects.all()

	p = Paginator(crime.objects.all().order_by("year"), 20)
	page = request.GET.get('page')
	crimes = p.get_page(page)
	nums = "a" * crimes.paginator.num_pages
	return render(request, 'crime/show_crime.html', 
		{'crime_list': crime_list,
		'crimes': crimes,
		'nums':nums}
		)