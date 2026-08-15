# from django.http import HttpResponse

# def billgates_bhavan(request):
#     return HttpResponse("Hello CSE students, Welcome to Bill Gates Bhavan")

from django.http import HttpResponse
from django.template import loader
from .models import BillGatesBhavan

def billgates_bhavan(request):
  bgbbhavan = BillGatesBhavan.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'bgbbhavan': bgbbhavan,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  bgbbhavan = BillGatesBhavan.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'bgbbhavan': bgbbhavan,
  }
  return HttpResponse(template.render(context, request))