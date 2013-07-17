from django.http import HttpResponseRedirect
from polls.models import Poll, Choice
from polls.forms import Create_poll, Create_choice
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.shortcuts import render

#function to view polls available on database
def index(request):
	qns = Poll.objects.all()
	choices = Choice.objects.all()	
	context ={'qns':qns,'choices':choices}   
	return render(request, 'polls/index.html', context) 


 #function to view choices for correponding poll   
def detail(request, poll_id):
	p=Poll.objects.get(id=poll_id)
	det=p.choice_set.all()	
	context ={'det':det}
	return render(request,'polls/details.html',context)

#function to remove a given poll	
def delete(request, poll_id):
	rempoll=Poll.objects.get(id=poll_id)
	rempoll.delete()
	word='wow you have delete item'	
	context ={'word':word}
	return render(request,'polls/message.html',context)
	
#to add poll
def create_poll(request):
	if request.POST:
	 form = Create_poll(request.POST)
	 if form.is_valid():
	    form.save()	    
         return HttpResponseRedirect('/')
        else:
		 form = Create_poll()
		 args = {}
		 args.update(csrf(request))
		 args[ 'form' ] = form
		 return render_to_response('polls/newpoll.html',args)
#to add choice on a given poll		 
def create_choice(request):
	if request.POST:
	 form = Create_choice(request.POST)
	 if form.is_valid():
	    form.save()	    
         return HttpResponseRedirect('/')
        else:
		 form = Create_choice()
		 args = {}
		 args.update(csrf(request))
		 args[ 'form' ] = form
		 return render_to_response('polls/newchoice.html',args)
		         
      
       

