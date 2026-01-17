from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Carz
from .forms import RentDetailsForm,FinalPriceForm
from userformapp.utils import send_email_view

# Create your views here.

@login_required(login_url='login')
def rental_cars(request,id=None):
    form = None
    if id:
        try:
            form = Carz.objects.get(id=id)
        except Carz.DoesNotExist:
            form = None
    seat = request.GET.get('seat')
    cars = Carz.objects.none()
    if seat:
        cars = Carz.objects.filter(seat_capacity = seat)
        
    return render(request,'rental/rentalcars.html',{"cars":cars,'form':form})
    
@login_required(login_url='login')
def details(request,id=0):
    form = Carz.objects.get(id=id)
    return render(request,'rental/details.html',{"form":form})

@login_required(login_url='login')
def rent_details(request,id=0):
    form = Carz.objects.get(id=id)
    seat = form.seat_capacity
    rupee = None
    if seat:
        if (form.fuel_type).lower() == 'petrol':
            rupee = 11 if seat == '5' else 16 if seat == '7' else None
        elif (form.fuel_type).lower() == 'diesel':
            rupee = 9 if seat == "5" else 14 if seat == "7" else None
        else:
            rupee = 13 if seat == "5" else 18 if seat == "7" else None

    form1 = RentDetailsForm()
    total_price = None
    if request.method == 'POST':
        form1 = RentDetailsForm(request.POST)
        if form1.is_valid():
            exp_km = form1.cleaned_data['expected_km']
            total_price = rupee * exp_km
        else:
            print("Form errors:", form1.errors)
    context = {
        'form':form,
        'form1':form1,
        'rupee':rupee,
        'total_price':total_price
        }
    return render(request,'rental/rent_details.html',context)

@login_required(login_url='login')
def final_price(request, id=0):
    form = Carz.objects.get(id=id)
    rupee = int(request.GET.get("rupee"))

    old_odometer = 5678
    km_allowed_per_day = 300

    fuel_prices = {"petrol": 102, "diesel": 90, "ev": 20}
    final_price_value = None

    form1 = FinalPriceForm()
    email = request.user.email
    if request.method == 'POST':
        form1 = FinalPriceForm(request.POST)
        if form1.is_valid():
            total_no_of_days = form1.cleaned_data['total_no_of_days']
            curr_odometer = form1.cleaned_data['km_drive_now']
            driven_km = curr_odometer - old_odometer

            base_cost = driven_km * rupee

            extra_km_ride = driven_km - (km_allowed_per_day * total_no_of_days)
            extra_cost = 0
            if extra_km_ride > 0:
                extra_cost = extra_km_ride * rupee

            net_cost = base_cost + extra_cost

            fuel_rate = fuel_prices.get(form.fuel_type.lower())
            fuel_cost = (driven_km / form.mileage) * fuel_rate

            if 1 <= extra_km_ride <= 500:
                net_cost = net_cost + (net_cost * 0.02)
                
            elif extra_km_ride > 500:
                net_cost = net_cost + (net_cost * 0.04)

            final_price_value = net_cost - fuel_cost

            response = send_email_view(email)
            print('email sent')
            return response

    context = {
        'form': form,
        'rupee': rupee,
        'odometer': old_odometer,
        'form1': form1,
        'final_price': round(final_price_value,2) if final_price_value is not None else None
    }
    return render(request, 'rental/final_price.html', context)
