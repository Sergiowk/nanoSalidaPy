from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, UpdateView
from .forms import DriversForm
from .models import Drivers
from django.urls import reverse_lazy

# Create your views here.
class DriversListView(View):
    def get(self, request, *args, **kwargs):
        
        drivers = Drivers.objects.all()
        # To get all this info we will need to pass it through the context 
        context={
            'drivers':drivers
        }
        return render(request, 'drivers.html', context)
    
class DriversDetailView(View):
    # In the get function we add the pk (primary key)
    def get(self, request, pk, *args, **kwargs):
        drivers = get_object_or_404(Drivers, pk=pk)
        context={
            'drivers':drivers
        }
        return render(request, 'drivers_details.html', context)

class DriversCreateView(View):
    def get(self, request, *args, **kwargs):
        form=DriversForm()
        context={
            #This is the context from forms.py, we are using the fields which appears there. 
            'form':form
        }
        return render(request, 'driver_form.html', context)
    
    def post(self, request, *args, **kwargs):
        if request.method=="POST":
            form = DriversForm(request.POST)
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
    
class DriversUpdateView(UpdateView):

    model=Drivers
    fields=['name', 'number', 'nationality', 'dob', 'comments']
    template_name='driver_update.html'

    # In case the update was done succesfully, we redirect to the details page for this driver 
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('drivers:drivers_details', kwargs={'pk':pk})