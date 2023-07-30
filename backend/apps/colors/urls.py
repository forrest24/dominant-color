from django.urls import path

from apps.colors.views import DominantColor

urlpatterns = [
    path('dominant_color/', DominantColor.as_view(), name='dominant-color'),
]