from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")
def detail(request, poll_id):
	return HttpResponse("you are looking at poll %s" % poll_id)
def results(request,poll_id):
	return HttpResponse("You are looking for the result at poll %s"%poll_id)
def vote(request, poll_id):
	return HttpResponse("you are voting on poll %s"%poll_id)
def chin(request, name):
	return HttpResponse("You are %"%name)
