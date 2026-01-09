from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from cars.models import Car
from cars.form import CarForm, CarModelForm
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView , DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
# function based views
def cars_view(request):
    cars = Car.objects.all().order_by('model')
    search = request.GET.get('search')

    if search:
        cars = Car.objects.filter(model__icontains=search)


    return render(
        request, 
        "cars.html", 
        {
            'cars': cars
            }
        )

# class based views
class CarsView(View):
    def get(self, request):
        cars = Car.objects.all().order_by('model')
        search = request.GET.get('search')

        if search:
            cars = Car.objects.filter(model__icontains=search)

        return render(
            request, 
            "cars.html", 
            {
                'cars': cars
                }
            )


#class list based views
class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')

        if search:
            cars = cars.filter(model__icontains=search)
        return cars
    






# function based views
def new_car_view(request):
    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
    else:
        new_car_form = CarModelForm()
    return render(
        request, 
        "new_car.html", 
        {"new_car_form": new_car_form}
    )


# class based views
class NewCarView(View):
    def get(self, request):
        new_car_form = CarModelForm()
        return render(
            request, 
            "new_car.html", 
            {"new_car_form": new_car_form}
        )

    def post(self, request):
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
        else:
            return render(
                request, 
                "new_car.html", 
                {"new_car_form": new_car_form}
            )


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'

#class list based views
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class NewCarViewCreate(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    template_name = 'car_update.html'
    form_class = CarModelForm

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required(login_url='/login/'), name='dispatch')   
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'