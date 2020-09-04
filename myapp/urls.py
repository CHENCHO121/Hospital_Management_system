from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('logout_admin', views.logout_admin, name='logout_admin'),
    path('view_doctor',views.view_doctor,name="view_doctor"),
    path('view_patient',views.view_patient,name="view_patient"),
    path('view_appointment',views.view_appointment,name="view_appointment"),
    path('add_doctor',views.add_doctor,name="add_doctor"),
    path('add_patient',views.add_patient,name="add_patient"),
    path('add_appointment',views.add_appointment,name="add_appointment"),
    path('delete_doctor/<int:pk>', views.delete_doctor, name="delete_doctor"),
    path('delete_patient/<int:pk>',views.delete_patient,name="delete_patient"),
    path('delete_appointment/<int:pk>',views.delete_appointment,name="delete_appointment"),
    path('edit_doctor/<int:pk>',views.edit_doctor,name="edit_doctor"),
    path('edit_patient/<int:pk>', views.edit_patient, name="edit_patient"),

]


