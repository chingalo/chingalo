from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from polls.models import Poll, Choice
from polls.forms import Create_poll
from django.shortcuts import render_to_response
from django.core.context_processors import csrf


#function to view polls available on database
def index(request):
	qns = Poll.objects.all()
	template = loader.get_template('polls/index.html')
	context = RequestContext(request,{'qns':qns})   
	return HttpResponse(template.render(context)) 


 #function to view choices for correponding poll   
def detail(request, poll_id):
	p=Poll.objects.get(id=poll_id)
	det=p.choice_set.all()
	template = loader.get_template('polls/details.html')
	context =RequestContext(request,{'det':det})
	return HttpResponse(template.render(context))

#function to remove a given poll	
def delete(request, poll_id):
	rempoll=Poll.objects.get(id=poll_id)
	rempoll.delete()
	word='wow you have delete item'
	template = loader.get_template('polls/message.html')
	context =RequestContext(request,{'word':word})
	return HttpResponse(template.render(context))
	
#to add poll
def create_poll(request):
	if request.POST:
	 form = Create_poll(request.POST)
	 if form.is_valid():
	    form.save()	    
         return HttpResponseRedirect('/polls/views/')
        else:
		 form = Create_poll()
		 args = {}
		 args.update(csrf(request))
		 args[ 'form' ] = form
		 return render_to_response('polls/newpoll.html',args)
		 
	         
      
       

