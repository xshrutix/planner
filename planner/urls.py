from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Temporary home view (can be replaced by a proper view or template)
def home(request):
    return HttpResponse("Welcome to the Monthly Challenges!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("challanges/", include("challanges.urls")),
    path("", home),  # Add this line to handle the empty path
]
