from django.http import HttpResponseRedirect
from polls.models import Poll, Choice
from polls.forms import Create_poll, Create_choice
from django.shortcuts import render_to_response, get_object_or_404, render
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse


#view polls
def index(request):
	qns = Poll.objects.all()
	choices = Choice.objects.all()	
	context ={'qns':qns,'choices':choices}   
	return render(request, 'polls/index.html', context)
	
	
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
		 
		 		         	 
 #edit a poll
def edit_poll(request, poll_id):	 
	 p=Poll.objects.get(id=poll_id)
	 context={'poll':p,'msg':'Edit a poll',} 
	 try:
		 edited_poll = request.POST['edit_poll']
	 except (KeyError, Choice.DoesNotExist):   
                  return render(request, 'polls/edit.html', context )       
         else:
		p.question=edited_poll
		p.save()
		return HttpResponseRedirect('/')
		

#to remove a given poll	
def delete(request, poll_id):
	rempoll=Poll.objects.get(id=poll_id)
	rempoll.delete()
	word='wow you have delete item'	
	context ={'word':word}
	return render(request,'polls/message.html',context)	
	
		
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
		 
		 
#to vote for a choice
def vote(request):
    polls=Poll.objects.all()
    choices=Choice.objects.all()
    #QueryDict: one of the key is choice
    dropdown=request.POST
    selected=dropdown.getlist('choice')
    a=len(selected)
    b=range(a)
    l=[] 
    for x in b:
		l.append(selected[x])
    for poll in polls:
		choices = poll.choice_set.filter(poll_id=poll.id)
		for x in l:				
			if x == '':
				l.remove(x)
				continue			
			else:
				for choice in choices:
				  if x == choice.choice_text:
					choice.vote +=1
					choice.save()
					l.remove(x)			
			
			break		
	
			
    context={'word':'Thank you very much for your voting....!!!'}
    return render(request, 'polls/message.html' ,context)        
        
# confirmation upon delete       
def warning(request, poll_id):
	poll=Poll.objects.get(id=poll_id)
	context={'poll':poll, 'msg':'Do you sure you want delete '}
	return render(request,'polls/warning.html',context)
	
	
#to view polls counts
def view_all(request):
	polls=Poll.objects.all()
	choices=Choice.objects.all()
	context={'polls':polls,'choices':choices,'value':0,}
	return render(request, 'polls/Views.html', context)

