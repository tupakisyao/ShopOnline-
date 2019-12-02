
from .models import Order

from . import utils

from django.core.mail import EmailMessage


def EMAILCreated(order_id):

    order = Order.objects.get(id=order_id)
    context = {
            "order_id" : order.id,
            "order_created": order.created,
            "order_first_name" : order.first_name,
            "order_last_name" : order.last_name,
            "order_email" : order.email,
            "order_address" : order.address,
            "order_post_code" : order.postal_code,
            "order_city" : order.city,

            "order_get_total_cost": order.get_total_cost()

        }






    send=EmailMessage('Order number {}'.format(order_id),'Dear, {}, you have successfully placed an order.\
               Your order number {}'.format(order.first_name, order.id), 'doszhan241@gmail.com', [order.email])


    pdf=utils.render_to_pdf('orders/order/pdf.html',context)
    send.attach('order_{}.pdf'.format(order.id),pdf,  'application/pdf')
    send.send()

    return None