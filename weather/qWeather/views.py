from django.http import HttpResponse


def index(request):
    output = "Hello, world. You're at the weather index."
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
