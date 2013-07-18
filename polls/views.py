from django.http import HttpResponseRedirect
from polls.models import Poll, Choice
from polls.forms import Create_poll, Create_choice
from django.shortcuts import render_to_response, get_object_or_404, render
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

#to vote for a choice
def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):  
        return render(request, 'polls/voting.html', {
            'poll': p,
            'message': "select a choice.",
        })
    else:
        selected_choice.vote += 1
        selected_choice.save()        
        return HttpResponseRedirect(reverse('choice_view', args=(p.id,)))

from django.shortcuts import get_object_or_404, render

def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})

def index(request):
	qns = Poll.objects.all()
	choices = Choice.objects.all()	
	context ={'qns':qns,'choices':choices}   
	return render(request, 'polls/index.html', context) 
#to view choices nad votes	   
def detail(request, poll_id):
	poll=Poll.objects.get(id=poll_id)
	det=poll.choice_set.all()	
	context ={'det':det,'poll':poll}
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
#to craete new choice		 
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
		         
      
       

