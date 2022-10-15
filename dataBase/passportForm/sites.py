from django.urls import path
from . import views

urlpatterns = [
    path('hi',views.save_data),
    path('show',views.show_page)
]