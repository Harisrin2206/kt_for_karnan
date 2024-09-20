from django.urls import path
from .import views

urlpatterns=[
    path('',views.user, name = 'home'),
    path('portfolio/<int:id>',views.portfolio)
]