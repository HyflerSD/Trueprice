from django.urls import path
from .views import HomePageView, ContactPageView, FeedBackPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('resources/contact', ContactPageView.as_view(), name='contact'),
    path('feedback/', FeedBackPageView.as_view(), name='feedback')
]