from django.urls import path, include
from .views import *

urlpatterns = [
    path('car/new/', CarEnter),
    path('car/leave/<int:pk>', CarLeaves),
]
