from django.http import HttpResponse
from django.template import RequestContext, loader
from polls.models import Poll, Choice
def index(request):
	qns = Poll.objects.all()
	template = loader.get_template('polls/index.html')
	context = RequestContext(request,{'qns':qns})   
	return HttpResponse(template.render(context)) 


    
def detail(request, poll_id):
	p=Poll.objects.get(id=poll_id)
	det=p.choice_set.all()
	template = loader.get_template('polls/details.html')
	context =RequestContext(request,{'det':det})
	return HttpResponse(template.render(context))
