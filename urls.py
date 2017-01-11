from django.conf.urls import url
from howdy import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^details/(?P<product_id>\d+)/$', views.Details), # Add this /about/ route
    url(r'^checkout/$', views.Checkout), 
    url(r'^addproduct/$', views.add_product), 
    url(r'^details/$', views.About), 
    url(r'^index/$', views.About), 
    
    
    
    
    
    ]