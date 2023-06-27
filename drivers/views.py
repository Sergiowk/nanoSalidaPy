from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import PostDriversForm
from .models import Drivers

# Create your views here.
class DriversListView(View):
    def get(self, request, *args, **kwargs):
        context={

        }
        return render(request, 'drivers.html', context)
    

class DriversCreateView(View):
    def get(self, request, *args, **kwargs):
        form=PostDriversForm()
        context={
            #This is the context from forms.py, we are using the fields which appears there. 
            'form':form
        }
        return render(request, 'driver_form.html', context)
    
    def post(self, request, *args, **kwargs):
        if request.method=="POST":
            form = PostDriversForm(request.POST)
            if form.is_valid():
                name=form.cleaned_data.get('name')          
                number=form.cleaned_data.get('number')            
                nationality=form.cleaned_data.get('nationality') 
                dob=form.cleaned_data.get('dob')          
                comments=form.cleaned_data.get('comments') 

                #Post created - assigning the values from the Drivers models to the value from the form
                p, created = Drivers.objects.get_or_create(name=name, number=number, nationality=nationality, dob=dob, comments=comments)
                p.save()
                return redirect('drivers:home_drivers')
        context={

        }
        return render(request, 'driver_form.html', context)