from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")
def detail(request, poll_id):
	return HttpResponse("you are looking at result %s" % poll_id)

def vote(request, poll_id):
	return HttpResponse("you are voting on poll %s"%poll_id)
