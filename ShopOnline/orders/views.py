
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import EMAILCreated
from django.urls import reverse
from django.shortcuts import render, redirect


def OrderCreate(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()


            EMAILCreated(order.id)
            request.session['order_id'] = order.id
            return redirect(reverse('payment:process'))


    form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart,
                                                        'form': form})


