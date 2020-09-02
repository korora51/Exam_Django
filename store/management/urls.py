from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('normal/', views.normal, name='normal'),
    path('forgetpass/', views.forgetpass, name='forgetpass'),
    path('legal_notice/', views.legal_notice, name='legal_notice'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('special_offer/', views.special_offer, name='special_offer'),
    path('store-details/', views.store_details, name='store-details'),
]