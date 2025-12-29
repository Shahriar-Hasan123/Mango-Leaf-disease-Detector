from django.urls import path
from .views import upload_image
from .views import history

urlpatterns = [
    path('', upload_image, name='upload'),
    path('history/', history, name='history'),

]
