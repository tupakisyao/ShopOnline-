from django.conf.urls import url
from . import views

app_name='payment'
urlpatterns = [
    url(r'^process/$', views.PaymentProcess, name='process'),
    url(r'^done/$', views.PaymentDone, name='done'),
    url(r'^canceled/$', views.PaymentCanceled, name='canceled')
]