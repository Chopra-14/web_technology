from django.http import HttpResponse
from django.template import loader

def baskara_bhavan(request):
    template = loader.get_template('baskara.html')
    return HttpResponse(template.render())