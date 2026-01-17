from django.shortcuts import render
from carapp.models import Company,Product
from django.contrib.auth.decorators import login_required
from carapp.forms import ProductEmiForm,TimeForm,EnquiryForm
from userformapp.forms import UserUpdateForm,UserProfileUpdateForm

# Create your views here.

@login_required(login_url='login')
def listofcomp(request):
    comp = Company.objects.all()
    return render(request,'cars/listofcomp.html',{'comp':comp})

@login_required(login_url='login')
def details(request,id=0):
    companies = Company.objects.get(id=id)
    return render(request,'cars/details.html',{'company':companies})

@login_required(login_url='login')
def calculate_emi(request,id=0):
    product = Product.objects.get(id=id)
    emi = None
    interest = {1:8.5,2:9.5,5:10.5,7:12,10:13.5}
    if request.method == 'POST':
        form = ProductEmiForm(request.POST,instance=product)
        if form.is_valid():
            loan_amount = form.cleaned_data['loan_amount']
            tenure = form.cleaned_data['tenure']
            
            interest_rate = interest[tenure]
            r = interest_rate / (12 * 100)
            n = tenure * 12
            emi = (loan_amount * r * (1 + r)**n) / ((1 + r)**n - 1)
    else:
        form = ProductEmiForm(instance=product)
    return render(request, 'cars/emi.html', {'form': form,'emi': round(emi, 2) if emi else None})

@login_required(login_url='login')
def interior_exterior_img(request,id=0):
    product= Product.objects.get(id=id)
    return render(request,'cars/interior_exterior_img.html',{'product':product})

@login_required(login_url='login')
def final_price(request,id=0):
    product = Product.objects.get(id=id)

    shw_price = product.price
    road_tax = shw_price * 0.08
    rto = shw_price * 0.05
    insurance = shw_price * 0.035
    gst = shw_price * 0.18
    miscellaneous = shw_price * 0.02

    total_price = road_tax + rto + insurance + gst + miscellaneous + shw_price

    context = {
        "shw_price":shw_price,
        "road_tax":road_tax,
        "rto":rto,
        "insurance":insurance,
        "gst":gst,
        "miscellaneous":miscellaneous,
        "total_price":total_price
    }

    return render(request,'cars/final_price.html',context)

@login_required(login_url='login')
def book_test_drive(request,id=0):
    product = Product.objects.get(id=id)
    form = ProductEmiForm(instance=product)
    form1 = UserProfileUpdateForm(instance=request.user)
    form2 = UserUpdateForm(instance=request.user.userdetails)
    form3 = TimeForm()
    submit = False
    dd= None
    time = None
    if request.method == 'POST':
        details = TimeForm(request.POST)
        if details.is_valid():
            dd = details.cleaned_data['date']
            time = details.cleaned_data['time']
            submit = True
        else:
            print("Form errors:", details.errors)
    else:
        form3 = TimeForm()
    context = {
        'form':form,
        'form1':form1,
        'form2':form2,
        "form3":form3,
        'submit':submit,
        'date':dd,
        'time':time,
        'product':product
        }
    return render(request,'cars/book_test_drive.html',context)

@login_required(login_url='login')
def enquiry_form(request, id=0):
    form = UserUpdateForm(instance=request.user)
    form1 = UserProfileUpdateForm(instance=request.user.userdetails)
    enquiry = False

    if request.method == 'POST':
        form2 = EnquiryForm(request.POST)
        if form2.is_valid():
            enquiry = True
    else:
        form2 = EnquiryForm()

    context = {
        'form': form,
        'form1': form1,
        'form2': form2,
        'enquiry': enquiry
    }
    return render(request, 'cars/enquiry_form.html', context)
