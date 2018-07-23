from django.http import HttpResponse


def robots(request):
    """ robot.txt <http://www.robotstxt.org>
    """
    return HttpResponse('User-agent: *\nDisallow: /')
