from django.urls import path
from .views import BookAPIView

urlpartterns = [
    path('', BookAPIView.as_view()),
]
