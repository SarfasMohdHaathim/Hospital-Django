from django.forms import ModelForm
from .models import *
from django import forms


class dateinput(forms.DateInput):
    input_type='date'

class BokkingForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        

        widgets={'booking_date':dateinput()}
        labels={
            'p_name':'Patient Name',
            'p_phone':'Patient Phone',
            'p_email':'Patient Email',
            'doc_name':'Doctor Name',
            'booking_date':'Booking Date'
            
        }
      

