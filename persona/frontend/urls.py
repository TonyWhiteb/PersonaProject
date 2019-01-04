from django.urls import path
from django.views.generic.base import RedirectView

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', RedirectView.as_view(url='persona/templates/base.html', permanent=False), name='index')
]