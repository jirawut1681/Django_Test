from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index),
    path('about',views.about),    # about คือ page      
    path('form',views.form),      # form คือ page         
    path('edit/<person_id>',views.edit), # edit คือ page 
    path('delete/<person_id>',views.delete) # delete คือ page 
]
