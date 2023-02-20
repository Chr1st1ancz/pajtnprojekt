from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from . import models
from django.http import HttpResponse
from django.template import loader
from .models import Member
def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        member = models.Member(filename=myfile.name)
        member.save()
        uploaded_file_url = fs.url(filename)
        return render(request, 'simple_upload.html', {
            'uploaded_file_url': uploaded_file_url,
            'mymembers': Member.objects.all().values()
        })
    return render(request, 'simple_upload.html')

def members(request):
  members = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': members,
  }
  return HttpResponse(template.render(context, request))