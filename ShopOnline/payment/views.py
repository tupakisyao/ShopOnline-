from django.core.mail import EmailMessage
from django.shortcuts import render, get_object_or_404

from django.conf import settings
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from orders.models import Order
from django.views.decorators.csrf import csrf_exempt


def PaymentProcess(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '%.2f' % order.get_total_cost(),

        'item_name': 'Заказ {}'.format(order.id),
        'invoice': str(order.id),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('payment:done')),
        'cancel_return': 'http://{}{}'.format(host, reverse('payment:canceled'))
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'payment/process.html',{'order':order, 'form':form})

@csrf_exempt
def PaymentDone(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    order.paid=True
    order.save()
    send = EmailMessage('Dear {}'.format(order.first_name), 'Thank you for choosing us.We have accepted your order. ', 'doszhan241@gmail.com', [order.email])
    send.send()
    return render(request, 'payment/done.html')

@csrf_exempt
def PaymentCanceled(request):
    return render(request, 'payment/canceled.html')