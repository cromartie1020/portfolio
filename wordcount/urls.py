from django.urls import path
from . import views
urlpatterns=[
   path('',views.setup,name='word_setup'),
   path('count/',views.count,name='count'),

]
