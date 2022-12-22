from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_school(request):
    form=SchoolForm()
    d={'form':form}
    if request.method=="POST":
        form_data=SchoolForm(request.POST)
        if form_data.is_valid():
            n=form_data.cleaned_data['name']
            p=form_data.cleaned_data['principal']
            L=form_data.cleaned_data['Location']
            S=SchoolInfo.objects.get_or_create(name=n,principal=p,Location=L)[0]
            S.save()
            return HttpResponse('data inserted successfully')

    return render(request,'insert_school.html',d)