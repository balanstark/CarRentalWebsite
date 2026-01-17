from django.urls import path
from rentalcars import views

urlpatterns = [
    path('',views.rental_cars,name='rentalcars'),
    path('<int:id>/', views.rental_cars, name='rentalcars_by_id'),
    path('details/<int:id>/',views.details,name='details'),
    path('rent_details/<int:id>/',views.rent_details,name='rent_details'),
    path('final_price/<int:id>',views.final_price,name='final_price')
]