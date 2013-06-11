from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime
from django.shortcuts import render
from personalblog.models import pblog
from django.shortcuts import render_to_response, get_object_or_404


def detail(request, blog_id):
    p = get_object_or_404(pblog, pk=blog_id)
    return render(request,'detail.html', {'blogentry': p})



def current_datetime (request):
	now = datetime.datetime.now()
	#t=get_template('current_datetime.html')
	#html = t.render(Context({'current_date':now}))
	#return HttpResponse(html)
	return render(request, 'current_datetime.html', {'current_date':now})



def about_me (request):
    return render(request, 'aboutme.html', {})

def future_tech (request):
    return render(request, 'futuretech.html', {})

def famous_quotes (request):
    return render(request, 'famousquotes.html', {})

def places (request):
    return render(request, 'places.html', {})

def fav_media (request):
    return render(request, 'favmedia.html', {})

def MyView(request):
    query_results = YourModel.objects.all()

def index(request):
    query_results = pblog.objects.all()
    
    return render(request,'blog.html',{
        'query_results': query_results,
    })









