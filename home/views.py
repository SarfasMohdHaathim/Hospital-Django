from django.shortcuts import render
from .models import *
from .forms import BokkingForm


# Create your views here.




def home(request):
    return render(request,'index.html')



def about(request):
    return render(request,'about.html')



def doctors(request):
    doc=Doctors.objects.all()
    context={'doc':doc}
    return render(request,'doctors.html',context)



def contact(request):
    return render(request,'contact.html')



def booking(request):
    if request.method =='POST':
        forms=BokkingForm(request.POST)
        if forms.is_valid():
                forms.save()
                return render(request, 'confrim.html')
    forms=BokkingForm()
    dic_form={
        'forms':forms
        }
    return render(request,'booking.html',dic_form)



def department(request):
    dept=Department.objects.all()
    context={'dept':dept}
    return render(request,'department.html',context)