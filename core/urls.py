from django.urls import path
from django.contrib.auth import views

from core.views import frontPage, shop, signup, myaccount, edit_myaccount
from product.views import product

urlpatterns = [
    path('', frontPage, name='frontPage'),
    path('signup/', signup, name='signup' ),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>/', product, name='product'),
    path('myaccount/edit/', edit_myaccount, name='edit_myaccount'),
    path('myaccount/', myaccount, name='myaccount')
]