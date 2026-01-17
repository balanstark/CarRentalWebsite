from django.urls import path
from . import views

urlpatterns = [
    path('',views.listofcomp,name='comp'),
    path('<int:id>',views.details,name='details'),
    path('emi/<int:id>',views.calculate_emi,name='emi'),
    path('interior_exterior_img/<int:id>',views.interior_exterior_img,name='interior_exterior_img'),
    path('final_price/<int:id>',views.final_price,name='final_price'),
    path('book_test_drive/<int:id>',views.book_test_drive,name='book_test_drive'),
    path('enquiry_form/<int:id>',views.enquiry_form,name='enquiry_form')
]