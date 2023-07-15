from django.urls import path
from .views import v_index

urlpatterns = [
    path('', v_index)
]