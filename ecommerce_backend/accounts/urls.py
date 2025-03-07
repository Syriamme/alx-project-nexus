from django.urls import path
from .views import register, login
from django.http import JsonResponse
def health_check(request):
    return JsonResponse({'status': 'ok'})

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('healthz/', health_check),
]
