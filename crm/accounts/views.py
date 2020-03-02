from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .form import OrderForm
from .form import CustomerForm
from .form import EventForm
from .filter import OrderFilter
from .filter import ProductFilter
from .form import AddProduct
from .form import UpdateProduct


# Create your views here.

def login(request):
    return render(request, 'accounts/login.html')


def register(request):
    return render(request, 'accounts/register.html')


def home(request):
    orders = Order.objects.all()
    customers = customer.objects.all()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    order_pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 'customers': customers,
               'total_orders': total_orders, 'delivered': delivered,
               'order_pending': order_pending}

    return render(request, 'accounts/dashboard.html', context)


def products(request):
    products = Products.objects.all()
    prodFilter = ProductFilter(request.GET, queryset=products)
    return render(request, 'accounts/products.html', {'products': products, 'prodFilter': prodFilter})


def ProductUpdate(request, pk):
    product_update = Products.objects.get(id=pk)
    form = UpdateProduct(instance=product_update)
    if request.method == "POST":
        form = UpdateProduct(request.POST, instance=product_update)
        if form.is_valid():
            form.save()
            return redirect('products')
    context = {'form': form, 'product': product_update}
    return render(request, 'accounts/productupdate.html', context)


def DeleteProduct(request, pk):
    product_delete = Products.objects.get(id=pk)
    if request.method == "POST":
        product_delete.delete()
        return redirect('products')
    context = {'product': product_delete}
    return render(request, 'accounts/deleteproduct.html', context)


def customer1(request, pk):
    customers = customer.objects.get(id=pk)
    orders = customers.order_set.all()
    order_count = orders.count()
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs
    context = {'customers': customers, 'orders': orders,
               'order_count': order_count,
               'myFilter': myFilter,
               }
    return render(request, 'accounts/customer.html', context)


def orders(request):
    order_delivered = Order.objects.filter(status='Delivered')
    pending_order = Order.objects.filter(status='Pending')
    context = {'order_delivered': order_delivered,
               'pending_order': pending_order}
    return render(request, 'accounts/orders.html', context)


def CreateOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        # print('Printing POST:' ,request.POST)

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def UpdateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def delete(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    context = {'item': order}
    return render(request, 'accounts/delete.html', context)


def CreateCustomer(request):
    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/customer_form.html', context)


def event(request):
    event1 = events.objects.all()
    context = {'event1': event1}
    return render(request, 'accounts/events.html', context)


def UpdateEvent(request):
    context = {}
    return render(request, 'accounts/updateevent.html', context)


def AddEvent(request):
    event1 = events.objects.all()
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST, event1)
        if form.is_valid():
            form.save()
            print("Event Saved Successfully")
            return redirect('event')
        print("Event Saved Successfully")
    context = {'form': form}
    return render(request, 'accounts/addevent.html', context)


def Addproduct(request):
    products = Products.objects.all()
    form = AddProduct()
    if request.method == "POST":
        form = AddProduct(request.POST, products)
        if form.is_valid():
            form.save()
            return redirect('products')
    context = {'form': form}
    return render(request, 'accounts/addproduct.html', context)


