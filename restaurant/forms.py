from django.forms import ModelForm
from .models import BookingTemplate


# Code added for loading form data on the Booking page
class BookingForm(ModelForm):
    class Meta:
        model = BookingTemplate
        fields = "__all__"
