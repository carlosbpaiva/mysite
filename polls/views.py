from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello %s. You're at the polls index"%request.user.username)
