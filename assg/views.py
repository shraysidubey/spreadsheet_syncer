from django.shortcuts import render
from assg.models import employee

def index(request):

    context_dict = {}

    emplyee_profile = employee.objects.all()
    context_dict['emplyee_profile'] = emplyee_profile

    return render(request, 'assg/index.html', context_dict)