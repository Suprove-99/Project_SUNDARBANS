from django.urls import path
from .views import HomePageView, WildLifeView, GuideView, SpotView ,BookingFormView

urlpatterns = [
    path('', HomePageView.as_view(), name='home_'),
    path('wildlife/', WildLifeView.as_view(), name='wildlife_'),
    path('guide/', GuideView.as_view(), name='guide_'),
    path('spot/', SpotView.as_view(), name='spot_'),
    path('form/',BookingFormView, name = 'form_')
]
