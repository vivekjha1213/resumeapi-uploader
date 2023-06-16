from django.urls import path
from api import views

urlpatterns = [
    # link the view post logic. to send the data client..
    path('resume/', views.ProfileView.as_view(), name='resume'),
    # Link the view post logic. to get the all data from database..
    path('list/', views.ProfileView.as_view(), name='list'),
]
