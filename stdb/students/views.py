from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Students
from django.urls import reverse

def index(request):
  mymembers = Students.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))
# Create your views here.
def jls_extract_def():
    return 
def addrecord(request):
  fname = request.POST["first"]
  lname = request.POST["last"]
  usn = request.POST["USN"]
  branch = request.POST["Branch"] 
  student = Students(firstname=fname,lastname=lname,enrollmentno=usn,specialization=branch)
  student.save()
  return HttpResponseRedirect(reverse(index))

def delete(request):
  template = loader.get_template('delete.html')
  return HttpResponse(template.render({},request))

def deleterecord(request):
  
  enrollmentno = request.POST['e_no']
  student = Students.objects.get(enrollmentno=enrollmentno)
  student.delete()
  return HttpResponseRedirect(reverse('index'))
