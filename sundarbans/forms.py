from django import forms
from django.forms import ModelForm
from .models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['package',
                  'name',
                  'country',
                  'email',
                  'phone',
                  'start_date',
                  'end_date'
        ]
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
        }
