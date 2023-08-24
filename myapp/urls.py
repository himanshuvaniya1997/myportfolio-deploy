from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('skill/',views.skill,name='skill'),
    path('portfolio/',views.portfolio,name='portfolio'),
    path('contact/',views.contact,name='contact'),
    path('project/',views.project,name='project'),
    path('photos/',views.photos,name='photos'),
    path('contact-data/',views.contact_data,name='contact-data'),

]
