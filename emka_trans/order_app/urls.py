
from django.conf.urls import url
from order_app import views

app_name = 'order_app'

urlpatterns = [
    url(r'^$',views.CheckoutListView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$',views.CheckoutDetailView.as_view(),name='detail'),
    url(r'^create/$',views.CheckoutCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.CheckoutUpdateView.as_view(),name='update'),
    #url(r'^product/(?P<pk>\d+)/$',views.OrderedProductsDetailView.as_view(),name='product_detail'),
    url(r'^update_product/(?P<pk>\d+)/$',views.ProductUpdateView.as_view(),name='update_product'),
    url(r'^delete/(?P<pk>\d+)/$',views.CheckoutDeleteView.as_view(),name='delete')
]