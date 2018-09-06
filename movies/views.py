from django.http import HttpResponse


def index(request):
    f = open('movies.txt', 'r')
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="text/plain")
