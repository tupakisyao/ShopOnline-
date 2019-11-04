from django.conf.urls import url
from . import views
app_name = 'shop'
urlpatterns = [
    url(r'^(?P<category_slug>[-\w]+)/$', views.ProductList, name='ProductListByCategory'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.ProductDetail, name='ProductDetail'),
    url(r'^$', views.ProductList, name='ProductList'),

]