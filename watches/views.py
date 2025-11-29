from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Watch, Order
from .forms import OrderForm

def catalog(request):
    watches = Watch.objects.all()
    return render(request, 'watches/catalog.html', {'watches': watches})

def watch_detail(request, watch_id):
    watch = get_object_or_404(Watch, id=watch_id)
    return render(request, 'watches/watch_detail.html', {'watch': watch})

def order_watch(request, watch_id):
    watch = get_object_or_404(Watch, id=watch_id)
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.watch = watch
            order.save()
            messages.success(request, f"Buyurtma muvaffaqiyatli qabul qilindi! {order.customer_phone} raqami orqali siz bilan bog'lanamiz.")
            return redirect('catalog')
    else:
        form = OrderForm()
    
    return render(request, 'watches/order_form.html', {'form': form, 'watch': watch})
